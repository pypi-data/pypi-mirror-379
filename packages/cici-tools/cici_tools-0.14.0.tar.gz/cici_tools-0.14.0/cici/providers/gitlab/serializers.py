# SPDX-FileCopyrightText: UL Research Institutes
# SPDX-License-Identifier: Apache-2.0

import copy
import io
import logging
import typing
from pathlib import Path
from typing import Optional

import cattrs
import ruamel.yaml

from ...config.project import models as cici_config
from ...utils import merge_dict
from . import models
from . import models as gitlab
from .converter import CONVERTER
from .utils import get_job_names


def expand_job_extends(jobs, job):
    job = copy.deepcopy(job)
    if not "extends" in job:
        return job

    extends = job["extends"]
    if isinstance(extends, str):
        extends = [extends]

    new_job = {}
    for extend in extends:
        new_job = merge_dict(new_job, expand_job_extends(jobs, jobs[extend]))
    new_job = merge_dict(new_job, job)
    del new_job["extends"]
    new_job = {key: value for key, value in sorted(new_job.items())}

    return new_job


def expand_jobs(data):
    jobs = data.setdefault("jobs", {})
    for job_name in list(jobs):
        jobs[job_name] = expand_job_extends(jobs, jobs[job_name])
    return data


def pack_jobs(data):
    job_names = get_job_names(data)
    jobs = {}
    for job_name in sorted(list(job_names)):
        if job_name.startswith("."):
            try:
                CONVERTER.structure(data[job_name], models.Job)
                jobs[job_name] = data[job_name]
            except (
                cattrs.errors.ClassValidationError,
                cattrs.errors.ForbiddenExtraKeysError,
            ) as excinfo:
                logging.warning(f"job {job_name} skipped")
                raise
            except (AttributeError,) as excinfo:
                if "CommentedSeq" in str(excinfo):
                    logging.warning(f"job {job_name} skipped")
                else:
                    raise
        else:
            jobs[job_name] = data[job_name]

        del data[job_name]
    data["jobs"] = jobs
    return data


def unpack_jobs(data: dict, cici_config_file: Optional[cici_config.File] = None):
    if "jobs" in data:
        jobs = data["jobs"]
        for name, job in jobs.items():
            data[name] = job
        del data["jobs"]

    inject_container_into_job(data, cici_config_file=cici_config_file)

    return data


def add_config_variables(data, cici_config_file):
    data.setdefault("variables", {})
    for name, variable in cici_config_file.variables.items():
        data["variables"][name] = {}
        data["variables"][name]["value"] = variable.default
        if variable.brief:
            data["variables"][name]["description"] = variable.brief
    return data


def inject_container_into_job(
    data: dict, cici_config_file: Optional[cici_config.File] = None
):
    if not cici_config_file:
        return

    # logging.info("Jobs avail for injection: %s", list(data.get("jobs", {}).keys()))
    jobs_dict = data.get("jobs", data)

    for target in cici_config_file.targets:
        # logging.info("Target: {target.name}, container={target.container}")
        if not target.container:
            continue
        if target.name not in jobs_dict:
            continue

        job = jobs_dict[target.name]

        # logging.info(f" Injecting into job {target.name}")
        job["image"] = {
            "name": target.container.image,
            "entrypoint": target.container.entrypoint,
        }


def loads(
    text: str, cici_config_file: typing.Optional[cici_config.File] = None
) -> gitlab.File:
    yaml = ruamel.yaml.YAML()
    data = yaml.load(text)
    if cici_config_file:
        data = add_config_variables(data, cici_config_file=cici_config_file)
    data = pack_jobs(data)
    data = expand_jobs(data)
    return CONVERTER.structure(data, gitlab.File)


def load(
    file: typing.Union[str, Path],
    cici_config_file: typing.Optional[cici_config.File] = None,
) -> gitlab.File:
    return loads(open(file).read(), cici_config_file=cici_config_file)


def dumps(
    file: gitlab.File, cici_config_file: typing.Optional[cici_config.File] = None
) -> str:
    output = io.StringIO()
    dump(file, output, cici_config_file)
    return output.getvalue()


def dump(
    file: gitlab.File,
    stream: typing.IO,
    cici_config_file: Optional[cici_config.File] = None,
):
    data = CONVERTER.unstructure(file)

    data = unpack_jobs(data, cici_config_file=cici_config_file)

    yaml = ruamel.yaml.YAML()
    yaml.default_flow_style = False
    yaml.explicit_start = False
    yaml.preserve_quotes = True
    yaml.indent(mapping=2, sequence=4, offset=2)

    blocks = [{key: value} for key, value in data.items()]
    fragments = []
    for block in blocks:
        text = io.StringIO()
        yaml.dump(block, text)
        fragments.append(text.getvalue().rstrip())
    stream.write("\n\n".join(fragments) + "\n")
