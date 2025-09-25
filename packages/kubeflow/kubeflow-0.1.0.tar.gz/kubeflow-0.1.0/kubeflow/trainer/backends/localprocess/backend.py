# Copyright 2025 The Kubeflow Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from collections.abc import Iterator
from datetime import datetime
import logging
import random
import string
import tempfile
from typing import Optional, Union
import uuid

from kubeflow.trainer.backends.base import ExecutionBackend
from kubeflow.trainer.backends.localprocess import utils as local_utils
from kubeflow.trainer.backends.localprocess.constants import local_runtimes
from kubeflow.trainer.backends.localprocess.job import LocalJob
from kubeflow.trainer.backends.localprocess.types import (
    LocalBackendJobs,
    LocalBackendStep,
    LocalProcessBackendConfig,
)
from kubeflow.trainer.constants import constants
from kubeflow.trainer.types import types

logger = logging.getLogger(__name__)


class LocalProcessBackend(ExecutionBackend):
    def __init__(
        self,
        cfg: LocalProcessBackendConfig,
    ):
        # list of running subprocesses
        self.__local_jobs: list[LocalBackendJobs] = []
        self.cfg = cfg

    def list_runtimes(self) -> list[types.Runtime]:
        return [self.__convert_local_runtime_to_runtime(local_runtime=rt) for rt in local_runtimes]

    def get_runtime(self, name: str) -> types.Runtime:
        runtime = next(
            (
                self.__convert_local_runtime_to_runtime(rt)
                for rt in local_runtimes
                if rt.name == name
            ),
            None,
        )
        if not runtime:
            raise ValueError(f"Runtime '{name}' not found.")

        return runtime

    def get_runtime_packages(self, runtime: types.Runtime):
        runtime = next((rt for rt in local_runtimes if rt.name == runtime.name), None)
        if not runtime:
            raise ValueError(f"Runtime '{runtime.name}' not found.")

        return runtime.trainer.packages

    def train(
        self,
        runtime: Optional[types.Runtime] = None,
        initializer: Optional[types.Initializer] = None,
        trainer: Optional[Union[types.CustomTrainer, types.BuiltinTrainer]] = None,
    ) -> str:
        # set train job name
        train_job_name = random.choice(string.ascii_lowercase) + uuid.uuid4().hex[:11]
        # localprocess backend only supports CustomTrainer
        if not isinstance(trainer, types.CustomTrainer):
            raise ValueError("CustomTrainer must be set with LocalProcessBackend")

        # create temp dir
        venv_dir = tempfile.mkdtemp(prefix=train_job_name)
        logger.debug(f"operating in {venv_dir}")

        runtime.trainer = local_utils.get_local_runtime_trainer(
            runtime_name=runtime.name,
            venv_dir=venv_dir,
            framework=runtime.trainer.framework,
        )

        # build training job command
        training_command = local_utils.get_local_train_job_script(
            trainer=trainer,
            runtime=runtime,
            train_job_name=train_job_name,
            venv_dir=venv_dir,
            cleanup_venv=self.cfg.cleanup_venv,
        )

        # set the command in the runtime trainer
        runtime.trainer.set_command(training_command)

        # create subprocess object
        train_job = LocalJob(
            name=f"{train_job_name}-train",
            command=training_command,
            execution_dir=venv_dir,
            env=trainer.env,
            dependencies=[],
        )

        self.__register_job(
            train_job_name=train_job_name,
            step_name="train",
            job=train_job,
            runtime=runtime,
        )
        # start the job.
        train_job.start()

        return train_job_name

    def list_jobs(self, runtime: Optional[types.Runtime] = None) -> list[types.TrainJob]:
        result = []

        for _job in self.__local_jobs:
            if runtime and _job.runtime.name != runtime.name:
                continue
            result.append(
                types.TrainJob(
                    name=_job.name,
                    creation_timestamp=_job.created,
                    runtime=runtime,
                    num_nodes=1,
                    steps=[
                        types.Step(name=s.step_name, pod_name=s.step_name, status=s.job.status)
                        for s in _job.steps
                    ],
                )
            )
        return result

    def get_job(self, name: str) -> Optional[types.TrainJob]:
        _job = next((j for j in self.__local_jobs if j.name == name), None)
        if _job is None:
            raise ValueError(f"No TrainJob with name {name}")

        # check and set the correct job status to match `TrainerClient` supported statuses
        status = self.__get_job_status(_job)

        return types.TrainJob(
            name=_job.name,
            creation_timestamp=_job.created,
            steps=[
                types.Step(name=_step.step_name, pod_name=_step.step_name, status=_step.job.status)
                for _step in _job.steps
            ],
            runtime=_job.runtime,
            num_nodes=1,
            status=status,
        )

    def get_job_logs(
        self,
        name: str,
        step: str = constants.NODE + "-0",
        follow: Optional[bool] = False,
    ) -> Iterator[str]:
        _job = [j for j in self.__local_jobs if j.name == name]
        if not _job:
            raise ValueError(f"No TrainJob with name {name}")

        want_all_steps = step == constants.NODE + "-0"

        for _step in _job[0].steps:
            if not want_all_steps and _step.step_name != step:
                continue
            # Flatten the generator and pass through flags so it behaves as expected
            # (adjust args if stream_logs has different signature)
            yield from _step.job.logs(follow=follow)

    def wait_for_job_status(
        self,
        name: str,
        status: set[str] = {constants.TRAINJOB_COMPLETE},
        timeout: int = 600,
        polling_interval: int = 2,
    ) -> types.TrainJob:
        # find first match or fallback
        _job = next((_job for _job in self.__local_jobs if _job.name == name), None)

        if _job is None:
            raise ValueError(f"No TrainJob with name {name}")
        # find a better implementation for this
        for _step in _job.steps:
            if _step.job.status in [constants.TRAINJOB_RUNNING, constants.TRAINJOB_CREATED]:
                _step.job.join(timeout=timeout)
        return self.get_job(name)

    def delete_job(self, name: str):
        # find job first.
        _job = next((j for j in self.__local_jobs if j.name == name), None)
        if _job is None:
            raise ValueError(f"No TrainJob with name {name}")

        # cancel all nested step jobs in target job
        _ = [step.job.cancel() for step in _job.steps]
        # remove the job from the list of jobs
        self.__local_jobs.remove(_job)

    def __get_job_status(self, job: LocalBackendJobs) -> str:
        statuses = [_step.job.status for _step in job.steps]
        # if status is running or failed will take precedence over completed
        if constants.TRAINJOB_FAILED in statuses:
            status = constants.TRAINJOB_FAILED
        elif constants.TRAINJOB_RUNNING in statuses:
            status = constants.TRAINJOB_RUNNING
        elif constants.TRAINJOB_CREATED in statuses:
            status = constants.TRAINJOB_CREATED
        else:
            status = constants.TRAINJOB_CREATED

        return status

    def __register_job(
        self,
        train_job_name: str,
        step_name: str,
        job: LocalJob,
        runtime: types.Runtime = None,
    ):
        _job = [j for j in self.__local_jobs if j.name == train_job_name]
        if not _job:
            _job = LocalBackendJobs(name=train_job_name, runtime=runtime, created=datetime.now())
            self.__local_jobs.append(_job)
        else:
            _job = _job[0]
        _step = [s for s in _job.steps if s.step_name == step_name]
        if not _step:
            _step = LocalBackendStep(step_name=step_name, job=job)
            _job.steps.append(_step)
        else:
            logger.warning(f"Step '{step_name}' already registered.")

    def __convert_local_runtime_to_runtime(self, local_runtime) -> types.Runtime:
        return types.Runtime(
            name=local_runtime.name,
            trainer=types.RuntimeTrainer(
                trainer_type=local_runtime.trainer.trainer_type,
                framework=local_runtime.trainer.framework,
                num_nodes=local_runtime.trainer.num_nodes,
                device_count=local_runtime.trainer.device_count,
                device=local_runtime.trainer.device,
            ),
            pretrained_model=local_runtime.pretrained_model,
        )
