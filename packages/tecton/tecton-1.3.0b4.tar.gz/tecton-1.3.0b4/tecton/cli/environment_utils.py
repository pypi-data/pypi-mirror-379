import logging
import os
import re
import subprocess
import sys
from pathlib import Path

from tecton_core.errors import FailedDependencyDownloadError


# need to list out compatible manylinux wheel for pip (https://github.com/pypa/pip/issues/10760)
COMPATIBLE_LINUX_PLATFORMS = [
    "manylinux1_x86_64",
    "manylinux_2_10_x86_64",
    "manylinux2010_x86_64",
    "manylinux_2_17_x86_64",
    "manylinux2014_x86_64",
    "manylinux_2_24_x86_64",
    "manylinux_2_28_x86_64",
    "manylinux_2_31_x86_64",
]

# additional wheel distributions for libs that do not have wheels in pypi
# For example we built a wheel for Pypika which Tecton depends on. (PyPika-0.48.9-py2.py3-none-any.whl)
ADDITIONAL_WHEELS_REPOS = ["https://s3.us-west-2.amazonaws.com/tecton.ai.public/python/index.html"]

PYTHON_VERSION_TO_PLATFORM = {
    "3.9": "x86_64-manylinux_2_31",
    "3.10": "x86_64-manylinux_2_31",
    "3.11": "x86_64-manylinux_2_31",
}

# Mapping from major.minor to full patch versions for pip download compatibility
# This matches the versions used in our base images
PYTHON_MAJOR_MINOR_TO_FULL_VERSION = {
    "3.9": "3.9.17",
    "3.10": "3.10.6",
    "3.11": "3.11.13",
}

MAX_ENVIRONMENTS_NAME_LENGTH = 60

logger = logging.getLogger(__name__)


def resolve_dependencies_uv(
    requirements_path: Path,
    resolved_requirements_path: Path,
    python_version: str,
    timeout_seconds: int,
):
    """Resolve dependencies using `uv`
    Parameters:
        requirements_path(Path): Path to the `requirements.txt` file
        resolved_requirements_path(Path): The target path for generating the fully resolved and pinned `resolved-requirements.txt` file
        python_version(str): The python version to resolve dependencies for
        timeout_seconds(int): The timeout in seconds for the dependency resolution
    """
    major_minor_version = _get_major_minor_version(python_version)
    if major_minor_version not in PYTHON_VERSION_TO_PLATFORM:
        msg = f"Invalid `python_version` {major_minor_version}. Expected one of: {list(PYTHON_VERSION_TO_PLATFORM.keys())}"
        raise ValueError(msg)
    platform = PYTHON_VERSION_TO_PLATFORM[major_minor_version]
    logger.debug(f"Resolving dependencies for platform: {platform} python-version: {major_minor_version}")

    _run_uv_compile(
        requirements_path=requirements_path,
        resolved_requirements_path=resolved_requirements_path,
        python_version=major_minor_version,
        platform=platform,
        timeout_seconds=timeout_seconds,
    )


def download_dependencies(requirements_path: Path, target_directory: Path, python_version: str):
    """
    Download wheels for all dependencies in a requirements.txt to a target directory
    Parameters:
        requirements_path(Path): Path to requirements.txt
        target_directory(Path): The target directory to download requirements to
        python_version(str): The python version to download dependencies for
    """
    # Map major.minor version to full patch version for pip download compatibility
    # pip needs the full version and the full version matches the python versioned used in our base images
    major_minor_version = _get_major_minor_version(python_version)
    full_python_version = PYTHON_MAJOR_MINOR_TO_FULL_VERSION.get(major_minor_version, python_version)

    command = _construct_download_command(
        target_path=target_directory, requirements_path=requirements_path, python_version=full_python_version
    )

    logger.debug(f"Executing command:\n {' '.join(command)}")

    result = subprocess.run(
        command,
        text=True,
    )
    if result.returncode != 0:
        raise FailedDependencyDownloadError(result.stderr)


def is_valid_environment_name(name: str) -> bool:
    # Only letters, numbers, hyphens, or underscores allowed in an environment name
    pattern = r"^[a-zA-Z0-9_-]+$"
    return bool(re.match(pattern, name)) and len(name) <= MAX_ENVIRONMENTS_NAME_LENGTH


def _get_major_minor_version(version: str):
    version_parts = version.split(".")
    return ".".join(version_parts[:2])


def _run_uv_compile(
    requirements_path: Path, resolved_requirements_path: Path, python_version: str, platform: str, timeout_seconds: int
):
    """Run the `uv pip compile` command to resolve and lock dependencies for specific platform and python version.
    Parameters:
        requirements_path(Path): Path to the `requirements.txt` file
        resolved_requirements_path(Path): The target path for generating the fully resolved and pinned `resolved-requirements.txt` file
        python_version(str): The python version to resolve dependencies for
        platform(str): The manylinux platform to resolve dependencies for
        timeout_seconds(int): The timeout in seconds for the uv command
    """
    command_list = [
        "pip",
        "compile",
        "--python-platform",
        platform,
        "--python-version",
        python_version,
        "--no-build",
        "--emit-find-links",
        "--emit-index-annotation",
        "--emit-index-url",
        "--no-strip-extras",
        str(requirements_path),
        "--output-file",
        str(resolved_requirements_path),
    ] + [item for repo in ADDITIONAL_WHEELS_REPOS for item in ("-f", repo)]

    uv_install_dir = os.getenv("UV_INSTALL_DIR")
    if uv_install_dir:
        uv_path = os.path.join(uv_install_dir, "uv")
    else:
        uv_path = "uv"

    command = [uv_path, *command_list]
    logger.debug(f"Executing command:\n {' '.join(command)}")

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
        )
    except subprocess.TimeoutExpired:
        error_message = f"Dependency Resolution timed out after {timeout_seconds} seconds! If problem persists, please contact Tecton Support for assistance."
        raise TimeoutError(error_message)
    if result.returncode != 0:
        raise ValueError(result.stderr)


def _construct_download_command(target_path: Path, requirements_path: Path, python_version: str):
    return [
        sys.executable,
        "-m",
        "pip",
        "download",
        "--no-deps",
        "-r",
        str(requirements_path),
        "-d",
        str(target_path),
        "--no-cache-dir",
        "--only-binary",
        ":all:",
        "--python-version",
        python_version,
        "--implementation",
        "cp",
    ] + [item for platform in COMPATIBLE_LINUX_PLATFORMS for item in ("--platform", platform)]
