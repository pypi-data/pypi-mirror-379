import logging
import os
import re
import shutil
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from dataclasses import dataclass
from pathlib import Path
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from urllib.parse import unquote
from urllib.parse import urlparse

import click
from packaging.requirements import Requirement
from pip._internal.req import parse_requirements
from tqdm import tqdm

from tecton import version
from tecton._internals import metadata_service
from tecton.cli import printer
from tecton.cli.cli_utils import display_principal
from tecton.cli.cli_utils import display_table
from tecton.cli.cli_utils import timestamp_to_string
from tecton.cli.command import TectonCommandCategory
from tecton.cli.command import TectonGroup
from tecton.cli.environment_utils import MAX_ENVIRONMENTS_NAME_LENGTH
from tecton.cli.environment_utils import download_dependencies
from tecton.cli.environment_utils import is_valid_environment_name
from tecton.cli.environment_utils import resolve_dependencies_uv
from tecton.cli.upload_utils import DEFAULT_MAX_WORKERS_THREADS
from tecton.cli.upload_utils import UploadPart
from tecton.cli.upload_utils import _get_directory_size
from tecton.cli.upload_utils import get_upload_parts
from tecton_core import http
from tecton_core import id_helper
from tecton_proto.common.container_image__client_pb2 import ContainerImage
from tecton_proto.data.remote_compute_environment__client_pb2 import ObjectStoreUploadPart
from tecton_proto.data.remote_compute_environment__client_pb2 import RemoteComputeType
from tecton_proto.data.remote_compute_environment__client_pb2 import RemoteEnvironmentStatus
from tecton_proto.data.remote_compute_environment__client_pb2 import RemoteEnvironmentUploadInfo
from tecton_proto.data.remote_compute_environment__client_pb2 import S3UploadInfo
from tecton_proto.data.remote_compute_environment__client_pb2 import S3UploadPart
from tecton_proto.remoteenvironmentservice.remote_environment_service__client_pb2 import CompletePackagesUploadRequest
from tecton_proto.remoteenvironmentservice.remote_environment_service__client_pb2 import CreateRemoteEnvironmentRequest
from tecton_proto.remoteenvironmentservice.remote_environment_service__client_pb2 import DeleteRemoteEnvironmentsRequest
from tecton_proto.remoteenvironmentservice.remote_environment_service__client_pb2 import GetPackagesUploadUrlRequest
from tecton_proto.remoteenvironmentservice.remote_environment_service__client_pb2 import ListRemoteEnvironmentsRequest
from tecton_proto.remoteenvironmentservice.remote_environment_service__client_pb2 import StartPackagesUploadRequest
from tecton_proto.remoteenvironmentservice.remote_environment_service__client_pb2 import UpdateRemoteEnvironmentRequest


RESOLVED_REQUIREMENTS_FILENAME = "resolved_requirements.txt"
TECTON_RIFT_MATERIALIZATION_RUNTIME_PACKAGE = "tecton"
TECTON_TRANSFORM_RUNTIME_PACKAGE = "tecton-runtime"
DEFAULT_ARCHITECTURE = "x86_64"
DEFAULT_PYTHON_VERSION = "3.9"

DEPENDENCY_RESOLUTION_TIMEOUT_SECONDS = 600
# The maximum size of all dependencies allowed for upload
MAX_ALLOWED_DEPENDENCIES_SIZE_GB = 10

MEGABYTE = 1024 * 1024
GIGABYTE = 1024 * MEGABYTE

CHECK_MARK = "✅"
ERROR_SIGN = "⛔"
ERROR_MESSAGE_PREFIX = "⛔ ERROR: "

logger = logging.getLogger(__name__)


@dataclass
class EnvironmentIdentifier:
    id: Optional[str]
    name: Optional[str]

    def __post_init__(self):
        if not self.id and not self.name:
            printer.safe_print(
                f"{ERROR_MESSAGE_PREFIX} At least one of `environment-id` or `name` must be provided", file=sys.stderr
            )
            sys.exit(1)

    def __str__(self):
        if self.id:
            return f"id: {self.id}"
        elif self.name:
            return f"name: {self.name}"
        else:
            return "No name or id set"

    def __eq__(self, identifier):
        if isinstance(identifier, EnvironmentIdentifier):
            if self.id:
                return self.id == identifier.id
            elif self.name:
                return self.name == identifier.name
        return False


@click.command("environment", cls=TectonGroup, command_category=TectonCommandCategory.INFRA)
def environment():
    """Manage Environments for Realtime and Rift job execution.

    Use `tecton --verbose environment` to print additional debug information with environment commands.
    """


@environment.command("list")
def list_environments():
    """List all available Python Environments"""
    remote_environments = _list_environments()
    _display_environments(remote_environments)


@environment.command("get")
@click.option("-i", "--environment-id", help="Environment Id", required=False, type=str)
@click.option("-n", "--name", help="Environment Name", required=False, type=str)
def get(environment_id: Optional[str] = None, name: Optional[str] = None):
    """Get Python Environment(s) matching a name or an ID"""
    environment_identifier = EnvironmentIdentifier(id=environment_id, name=name)
    remote_environments = _list_environments(environment_identifier=environment_identifier)
    if len(remote_environments) < 1:
        error_message = f"⛔ Could not find a match for environment with {environment_identifier.__str__()}!"
        printer.safe_print(error_message, file=sys.stderr)
        sys.exit(1)
    elif len(remote_environments) > 1:
        error_message = f"⚠️ Could not find an exact match for environment with {environment_identifier.__str__()}. Did you mean one of the following?"
        printer.safe_print(error_message, file=sys.stderr)
        _display_environments(remote_environments)
    else:
        _display_environments(remote_environments, verbose=True)


@environment.command("resolve-dependencies")
@click.option("-r", "--requirements", help="Path to a requirements file", required=True, type=click.Path(exists=True))
@click.option(
    "-o",
    "--output-file",
    help="Output file to write resolved and fully pinned requirements to. If not specified, the pinned requirements will be printed to stdout",
    required=False,
    type=click.Path(exists=False),
)
@click.option(
    "-p",
    "--python-version",
    help=f"Python Version for the environment, defaults to {DEFAULT_PYTHON_VERSION}",
    required=False,
)
def resolve_requirements(
    requirements: str,
    output_file: Optional[str] = None,
    python_version: Optional[str] = None,
):
    """Resolve dependencies and return a fully resolved set of requirements for a given requirements.txt"""
    _python_version = python_version or DEFAULT_PYTHON_VERSION

    with tempfile.TemporaryDirectory() as tmpdir:
        try:
            resolved_requirements_path, _, _ = _run_dependency_resolution(
                requirements_path=Path(requirements),
                resolved_requirements_directory=Path(tmpdir),
                python_version=_python_version,
            )
        except ValueError as e:
            printer.safe_print(f"{ERROR_MESSAGE_PREFIX} {e}", file=sys.stderr)
            sys.exit(1)

        if output_file is not None:
            output_path = Path(output_file)
            resolved_requirements_str = resolved_requirements_path.read_bytes()
            output_path.write_bytes(resolved_requirements_str)
        else:
            printer.safe_print("\n🎉 Fully Resolved Requirements: \n")
            _display_requirements(requirements_path=resolved_requirements_path)


@environment.command("create")
@click.option("-n", "--name", help="Name of the environment", required=True, type=str)
@click.option(
    "-r",
    "--requirements",
    help="Path to the requirements.txt file containing all dependencies for the environment",
    required=True,
    type=click.Path(exists=True),
)
@click.option("-d", "--description", help="A description for the environment", required=False, type=str)
@click.option(
    "-p",
    "--python-version",
    help=f"Python Version for the environment, defaults to {DEFAULT_PYTHON_VERSION}",
    required=False,
)
def create(
    name: str,
    requirements: str,
    description: Optional[str] = None,
    python_version: Optional[str] = None,
):
    """Create a custom Tecton Rift job Environment."""
    return _create(name, requirements, description, python_version)


def _create(
    name: str,
    requirements: str,
    description: Optional[str] = None,
    python_version: Optional[str] = None,
):
    """Create a custom Tecton Rift job Environment."""
    _python_version = python_version or DEFAULT_PYTHON_VERSION
    if not is_valid_environment_name(name):
        printer.safe_print(
            f"{ERROR_MESSAGE_PREFIX} Invalid name.\nCustom environment names can only contain letters, numbers, hyphens, and underscores.\nNames must be no more than {MAX_ENVIRONMENTS_NAME_LENGTH} characters long.",
            file=sys.stderr,
        )
        sys.exit(1)

    environment_names = [e.name for e in _list_environments()]
    if name in environment_names:
        printer.safe_print(
            f"{ERROR_MESSAGE_PREFIX} An environment with the name `{name}` already exists in Tecton!",
            file=sys.stderr,
        )
        sys.exit(1)

    resp = _create_environment_with_requirements(
        name,
        description,
        Path(requirements),
        _python_version,
    )
    if resp:
        _display_environments([resp.remote_environment])
        printer.safe_print(
            f"\n🎉 Successfully created environment {name} with Status=PENDING. Please run `tecton environment get --name <environment-name>` to monitor the status of the environment"
        )


@environment.command("describe")
@click.option("-i", "--environment-id", help="Environment ID", required=False, type=str)
@click.option("-n", "--name", help="Environment Name", required=False, type=str)
def describe(environment_id: Optional[str] = None, name: Optional[str] = None):
    """
    Print additional information about an environment
    """
    environment_identifier = EnvironmentIdentifier(id=environment_id, name=name)
    environments = _list_environments(environment_identifier)
    if not environments:
        error_message = f"⛔ Could not find a match for environment with {environment_identifier.__str__()}!"
        printer.safe_print(error_message, file=sys.stderr)
        sys.exit(1)
    if len(environments) > 1:
        message = (
            f"Could not find environment with {environment_identifier.__str__()}. Did you mean one of the following?"
        )
        printer.safe_print(f"⚠️ {message}")
        _display_environments(environments)
    else:
        environment_match = environments[0]
        printer.safe_print("\n💡 Environment Details: \n")
        _display_environments(environments, verbose=True)
        printer.safe_print("\n💡 Input Requirements: \n")
        _display_requirements(requirements_str=environment_match.requirements)
        printer.safe_print("\n✅ Fully Resolved Requirements: \n")
        _display_requirements(requirements_str=environment_match.resolved_requirements)


@environment.command("search")
@click.option("-p", "--package", help="Package name to search for (exact match)", required=True, type=str)
@click.option(
    "-v", "--version", help="Version constraint (e.g., '1.2.3', '<2.0.0', '>=1.5,<2.0')", required=False, type=str
)
def search(package: str, version: Optional[str] = None):
    """Search environments by their resolved requirements.

    Examples:
      tecton environment search --package pandas --version ">=1.0,<2.0"
      tecton environment search --package numpy
      tecton environment search --package requests
    """
    environments = _list_environments()
    matches = _search_environments_by_requirements(environments=environments, package=package, version=version)

    if not matches:
        printer.safe_print("🔍 No environments found matching the search criteria.")
        return

    printer.safe_print(f"🔍 Found {len(matches)} environment(s) matching the search criteria:\n")
    _display_search_results(matches)


@environment.command("delete")
@click.option("-i", "--environment-id", help="Environment ID", required=False, type=str)
@click.option("-n", "--name", help="Environment Name", required=False, type=str)
def delete(environment_id: Optional[str] = None, name: Optional[str] = None):
    """Delete an existing custom Python Environment by name or ID"""
    return _delete(environment_id=environment_id, name=name)


def _delete(environment_id: Optional[str] = None, name: Optional[str] = None, skip_confirmation: bool = False):
    """Delete an existing custom Python Environment by name or ID"""
    environment_identifier = EnvironmentIdentifier(id=environment_id, name=name)
    environments = _list_environments(environment_identifier=environment_identifier)
    if not environments:
        printer.safe_print(
            f"⛔ No matching environment found for: {environment_identifier.__str__()}. Please verify available environments using the `tecton environment list` command",
            file=sys.stderr,
        )
        sys.exit(1)
    result_identifier = None
    environment_to_delete = None
    if len(environments) == 1:
        environment_to_delete = environments[0]
        result_identifier = EnvironmentIdentifier(id=environment_to_delete.id, name=environment_to_delete.name)

    if len(environments) > 1 or not environment_identifier.__eq__(identifier=result_identifier):
        printer.safe_print(
            f"⚠️ No matching environment found for: {environment_identifier.__str__()}. Did you mean one of the following environment(s)? \n\n",
            file=sys.stderr,
        )
        _display_environments(environments)
    else:
        confirmation_text = f"⚠️  Are you sure you want to delete environment {environment_to_delete.name}? (y/n) :"
        confirmation = "y" if skip_confirmation else input(confirmation_text).lower().strip()
        if confirmation == "y":
            try:
                delete_environment(environment_id=environment_to_delete.id)
                printer.safe_print(f"✅ Marked environment '{environment_identifier.__str__()}' for deletion.")
            except Exception as e:
                printer.safe_print(f"⛔ Failed to delete environment. error = {str(e)}, type= {type(e).__name__}")
        else:
            printer.safe_print(f"Cancelled deletion for environment: {environment_identifier.__str__()}")


def _display_environments(environments: List, verbose: bool = False):
    headings = [
        "Id",
        "Name",
        "Type",
        "Status",
        "Materialization Version",
        "Tecton Runtime Version",
        "Created By",
        "Created At",
        "Batch Image URI",
    ]
    if verbose:
        headings.extend(["Description", "Status Details"])

    rows = []
    for i in environments:
        row = (
            i.id,
            i.name,
            RemoteComputeType.Name(i.type).split("_")[-1],
            RemoteEnvironmentStatus.Name(i.status).split("_")[-1],
            i.rift_batch_job_environment.tecton_materialization_runtime_version or "N/A",
            i.realtime_job_environment.tecton_transform_runtime_version or "N/A",
            display_principal(i.created_by_principal),
            timestamp_to_string(i.created_at),
            i.rift_batch_job_environment.image_info.image_uri or "N/A",
        )
        if verbose:
            row += (i.description or "N/A", i.status_details or "N/A")

        rows.append(row)

    display_table(headings, rows)


def _create_environment_with_image(name: str, description: str, image_uri):
    try:
        req = CreateRemoteEnvironmentRequest()
        req.name = name
        req.description = description

        image_info = ContainerImage()
        image_info.image_uri = image_uri

        req.image_info.CopyFrom(image_info)

        return metadata_service.instance().CreateRemoteEnvironment(req)
    except PermissionError as _:
        printer.safe_print(
            "The user is not authorized to create environment(s) in Tecton. Please reach out to your Admin to complete this "
            "action",
            file=sys.stderr,
        )
        sys.exit(1)
    except Exception as e:
        printer.safe_print(f"⛔ Failed to create environment: {e}", file=sys.stderr)
        sys.exit(1)


def _create_environment_with_requirements(
    name: str,
    description: str,
    requirements_path: Path,
    python_version: str,
):
    """Create a custom environment by resolving dependencies, downloading wheels and updating MDS
    Parameters:
        name(str): Name of the custom environment
        description(str): Description of the custom environment
        requirements_path(str): Path to the `requirements.txt` file
        python_version(str): The Python version to resolve the dependencies for
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        try:
            resolved_requirements_path, tecton_runtime_version, tecton_rift_version = _run_dependency_resolution(
                requirements_path=requirements_path,
                resolved_requirements_directory=Path(tmpdir),
                python_version=python_version,
            )
        except ValueError as e:
            printer.safe_print(f"{ERROR_MESSAGE_PREFIX} {e}", file=sys.stderr)
            sys.exit(1)

        assert tecton_runtime_version or tecton_rift_version, (
            f"`tecton-runtime` and/or `tecton[rift-materialization]` must be specified in the resolved requirements: \n{resolved_requirements_path.read_text()}"
        )

        printer.safe_print(
            f"\n💡 Creating environment '{name}' for job types:\n"
            f"{CHECK_MARK if tecton_runtime_version else ERROR_SIGN} Realtime\n"
            f"{CHECK_MARK if tecton_rift_version else ERROR_SIGN} Rift Batch\n"
            f"{CHECK_MARK if tecton_rift_version and tecton_runtime_version else ERROR_SIGN} Rift Stream Ingest\n"
        )

        download_wheels_dir = Path(tmpdir) / "wheels"
        download_wheels_dir.mkdir()
        printer.safe_print("\n⏳ Downloading wheels. This may take a few seconds.....\n")
        download_dependencies(
            requirements_path=resolved_requirements_path,
            target_directory=download_wheels_dir,
            python_version=python_version,
        )
        printer.safe_print("\n✅ Successfully downloaded dependencies")

        directory_size = _get_directory_size(download_wheels_dir)
        if directory_size > (MAX_ALLOWED_DEPENDENCIES_SIZE_GB * GIGABYTE):
            printer.safe_print(
                f"{ERROR_MESSAGE_PREFIX} The total size of the downloaded dependencies exceeds the max allowed limit of {MAX_ALLOWED_DEPENDENCIES_SIZE_GB}GB. Please reduce the total number / size of dependencies and try again!",
                file=sys.stderr,
            )
            sys.exit(1)

        printer.safe_print("\n⏳ Uploading compressed wheels in parts to S3. This may take a few seconds.....")
        environment_id = id_helper.IdHelper.generate_string_id()
        try:
            location = _upload_dependencies(source_path=download_wheels_dir, environment_id=environment_id)
        except ValueError as e:
            printer.safe_print(f"{ERROR_MESSAGE_PREFIX} Unable to upload dependencies - {e}", file=sys.stderr)
            sys.exit(1)

        return create_remote_environment(
            name=name,
            id=environment_id,
            description=description,
            python_version=python_version,
            s3_wheels_location=location,
            requirements=requirements_path.read_text(),
            resolved_requirements=resolved_requirements_path.read_text(),
            transform_runtime_version=tecton_runtime_version,
            rift_materialization_runtime_version=tecton_rift_version,
            sdk_version=version.get_semantic_version(),
        )


def create_remote_environment(**kwargs):
    req = CreateRemoteEnvironmentRequest(**kwargs)
    return metadata_service.instance().CreateRemoteEnvironment(req)


def update_environment_status(**kwargs):
    req = UpdateRemoteEnvironmentRequest(**kwargs)
    return metadata_service.instance().UpdateRemoteEnvironment(req)


def _validate_input_requirements(input_requirements_path: Path):
    reqs = parse_requirements(str(input_requirements_path), session=None)
    for req in reqs:
        requirement_str = req.requirement
        try:
            parsed_req = Requirement(requirement_str)
        except Exception:
            # If we cannot parse the line as a standard requirement, skip it
            continue

        package_name = parsed_req.name
        extras = set(parsed_req.extras or [])

        # Accept either:
        # - tecton-runtime (no extras necessary)
        # - tecton with rift-materialization extra, even if other extras are present
        if package_name == TECTON_TRANSFORM_RUNTIME_PACKAGE:
            return
        if package_name == TECTON_RIFT_MATERIALIZATION_RUNTIME_PACKAGE and "rift-materialization" in extras:
            return

    printer.safe_print(
        f"{ERROR_MESSAGE_PREFIX} Please include at least one of the supporting Tecton libraries:\n"
        f"💡  `tecton-runtime` package (https://pypi.org/project/tecton-runtime) to support Realtime environments\n"
        f"💡  `tecton\\[rift-materialization]` package (https://pypi.org/project/tecton) to support Rift materialization environments\n",
        "\nFor more information, please see: https://docs.tecton.ai/docs/materializing-features/configure-rift-materialization/python-rift-environments",
        file=sys.stderr,
    )
    sys.exit(1)


def _get_pkg_to_version(resolved_requirements_file: Path, packages: List[str]) -> Dict[str, str]:
    version_pattern = re.compile(r"==([\w.\-]+)")
    file_pattern = re.compile(r"@ (file|https?)://(.+)", re.IGNORECASE)
    wheel_version_pattern = re.compile(r"([\w.\-]+)-([\d.]+.*?)(-py\d|\.tar\.gz|\.zip|\.whl)")
    package_versions = {}

    # Preprocess the target packages to support matching by normalized name and required extras
    targets_by_name = {}
    for pkg_spec in packages:
        pkg_req = Requirement(pkg_spec)
        target_name = pkg_req.name
        target_required_extras = set(pkg_req.extras)
        if target_name in targets_by_name:
            msg = f"Duplicate target specified for package '{target_name}' with extras {target_required_extras}."
            raise ValueError(msg)
        targets_by_name[target_name] = (target_required_extras, pkg_spec)

    reqs = parse_requirements(str(resolved_requirements_file), session=None)

    for req in reqs:
        requirement = req.requirement.strip()

        # Normalize the package name using packaging to strip extras for matching
        try:
            parsed_req = Requirement(requirement)
            normalized_name = parsed_req.name
            actual_extras = set(parsed_req.extras)
        except Exception:
            # Skip non-requirement or unparsable lines (indexes, options, comments)
            continue

        # Split the requirement to extract the version/source info
        if "==" in requirement:
            _, version_info = requirement.split("==", 1)
        elif "@" in requirement:
            _, version_info = requirement.split("@", 1)
        else:
            version_info = None

        # See if this requirement matches any of the requested targets for this name,
        # respecting required extras (subset match).
        if normalized_name in targets_by_name:
            tecton_version = None

            # Check for version specified with '=='
            if version_info and version_pattern.search(requirement):
                tecton_version = version_pattern.search(requirement).group(1)
            # Check for '@ file://' or '@ https://' notation
            elif version_info and file_pattern.search(requirement):
                file_match = file_pattern.search(requirement)
                url = file_match.group(0).split("@", 1)[1].strip()
                parsed_url = urlparse(url)
                wheel_filename = os.path.basename(parsed_url.path)
                wheel_filename = unquote(wheel_filename)
                # Extract version from the wheel filename
                wheel_match = wheel_version_pattern.match(wheel_filename)
                if wheel_match:
                    tecton_version = wheel_match.group(2)
            # Case 3: Direct URL to wheel file without '==' or '@'
            elif requirement.startswith("https://"):
                parsed_url = urlparse(requirement)
                wheel_filename = os.path.basename(parsed_url.path)
                wheel_filename = unquote(wheel_filename)
                # Extract package name and version from the wheel filename
                wheel_match = wheel_version_pattern.match(wheel_filename)
                if wheel_match:
                    package_name = wheel_match.group(1)
                    tecton_version = wheel_match.group(2)

            if tecton_version:
                required_extras, key_str = targets_by_name[normalized_name]
                if required_extras.issubset(actual_extras) or not required_extras:
                    package_versions[key_str] = tecton_version
            else:
                printer.safe_print(
                    f"⛔ Failed to parse version from tecton requirement:\n {requirement}\n"
                    f"Check for '==', '@ file://', '@ https://' notations",
                    file=sys.stderr,
                )
                sys.exit(1)

    return package_versions


def _run_dependency_resolution(
    requirements_path: Path, resolved_requirements_directory: Path, python_version: str
) -> Tuple[Path, str, str]:
    """
    :param requirements_path: input requirements file path to be resolved
    :param resolved_requirements_directory: where to resolve the requirements file
    :param python_version: python version to resolve against
    :return: resolved_requirements_path, tecton_runtime_version, tecton_rift_materialization_version

    """
    _validate_input_requirements(requirements_path)
    printer.safe_print(
        f"\n⏳ Resolving dependencies for Python {python_version} and architecture {DEFAULT_ARCHITECTURE} using uv. This may take a few seconds....."
    )
    resolved_requirements_path = resolved_requirements_directory / RESOLVED_REQUIREMENTS_FILENAME

    resolve_dependencies_uv(
        python_version=python_version,
        requirements_path=requirements_path,
        resolved_requirements_path=resolved_requirements_path,
        timeout_seconds=DEPENDENCY_RESOLUTION_TIMEOUT_SECONDS,
    )
    tecton_pkg_to_version = _get_pkg_to_version(
        resolved_requirements_path, packages=["tecton[rift-materialization]", "tecton-runtime"]
    )
    tecton_runtime_version = tecton_pkg_to_version.get("tecton-runtime")
    tecton_rift_version = tecton_pkg_to_version.get("tecton[rift-materialization]")

    printer.safe_print(
        "\n💡 Tecton versions:\n" + "\n".join(f"{pkg}: {vers}" for pkg, vers in tecton_pkg_to_version.items())
    )
    printer.safe_print("\n✅ Successfully resolved dependencies")
    return resolved_requirements_path, tecton_runtime_version, tecton_rift_version


def delete_environment(environment_id: str):
    try:
        req = DeleteRemoteEnvironmentsRequest()
        req.ids.append(environment_id)
        return metadata_service.instance().DeleteRemoteEnvironments(req)
    except PermissionError as _:
        printer.safe_print(
            "⛔ The user is not authorized to perform environment deletion. Please reach out to your Admin to complete this action.",
            file=sys.stderr,
        )
        sys.exit(1)
    except Exception as e:
        printer.safe_print(f"⛔ Failed to delete environment: {e}", file=sys.stderr)
        sys.exit(1)


def _list_environments(environment_identifier: Optional[EnvironmentIdentifier] = None) -> List:
    try:
        req = ListRemoteEnvironmentsRequest()
        response = metadata_service.instance().ListRemoteEnvironments(req)
        if not environment_identifier:
            return list(response.remote_environments)
        if environment_identifier.id:
            environments = [env for env in response.remote_environments if environment_identifier.id in env.id]
        else:
            # Look for an exact match. If there are no exact matches, we will return all substring matches
            environments = [env for env in response.remote_environments if environment_identifier.name == env.name]
            if not environments:
                environments = [env for env in response.remote_environments if environment_identifier.name in env.name]

        return environments

    except Exception as e:
        printer.safe_print(f"⛔ Failed to fetch environments: {e}", file=sys.stderr)
        sys.exit(1)


def _upload_dependencies(source_path: Path, environment_id: str) -> str:
    """Upload dependencies from the specified source path to S3.

    Args:
        source_path (str): The path to the dependencies to upload.
        environment_id (str): The ID of the environment.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        output_zip_file = Path(tmpdir) / "wheels.zip"
        logger.debug(f"Zipping dependencies at {output_zip_file}")

        shutil.make_archive(str(output_zip_file.with_suffix("")), "zip", str(source_path))
        file_size = output_zip_file.stat().st_size

        logger.debug("Initiating Multi-Part Upload")
        start_request = StartPackagesUploadRequest(environment_id=environment_id)
        start_response = metadata_service.instance().StartPackagesUpload(start_request)

        upload_id = start_response.upload_info.s3_upload_info.upload_id
        upload_parts = _upload_file_in_parts(
            file_size=file_size,
            upload_id=upload_id,
            environment_id=environment_id,
            output_zip_file=output_zip_file,
        )

        complete_request = CompletePackagesUploadRequest(
            upload_info=RemoteEnvironmentUploadInfo(
                environment_id=environment_id,
                s3_upload_info=S3UploadInfo(upload_id=upload_id, upload_parts=upload_parts),
            )
        )
        complete_response = metadata_service.instance().CompletePackagesUpload(complete_request)
        location = complete_response.storage_location
        printer.safe_print("✅ Successfully uploaded dependencies")
        return location


def _upload_file_in_parts(
    file_size: int, upload_id: str, environment_id: str, output_zip_file: Path
) -> List[S3UploadPart]:
    """Upload a file in parallel, dividing it into parts.

    Args:
        file_size (int): The size of the file in bytes.
        upload_id (str): A unique identifier for the file upload, returned by S3.
        environment_id (str): The ID of the environment.
        output_zip_file (str): The path to the file to upload.

    Returns:
        list: A list of upload part results.
    """
    # Calculate all parts for multi part upload
    part_data_list = get_upload_parts(file_size=file_size)
    with ThreadPoolExecutor(DEFAULT_MAX_WORKERS_THREADS) as executor:
        upload_futures = [
            executor.submit(
                _upload_part,
                upload_part=part_data,
                parent_upload_id=upload_id,
                environment_id=environment_id,
                dependency_file_path=output_zip_file,
            )
            for part_data in part_data_list
        ]
        with tqdm(total=len(part_data_list), desc="Upload progress", ncols=100) as pbar:
            for future in as_completed(upload_futures):
                # Increment the tqdm progress bar whenever a future is done
                if future.result():
                    pbar.update(1)

        return [future.result() for future in upload_futures]


def _upload_part(
    upload_part: UploadPart,
    parent_upload_id: str,
    environment_id: str,
    dependency_file_path: str,
):
    """Upload a part of a file.

    Args:
        upload_part (UploadPart): The part to upload.
        parent_upload_id (str): The ID of the parent upload.
        environment_id (str): The ID of the environment.
        dependency_file_path (str): The path to the file to upload.

    Returns:
        S3UploadPart: An object representing the uploaded part.
    """
    request = GetPackagesUploadUrlRequest(
        environment_id=environment_id,
        upload_part=ObjectStoreUploadPart(
            s3_upload_part=S3UploadPart(parent_upload_id=parent_upload_id, part_number=upload_part.part_number)
        ),
    )
    response = metadata_service.instance().GetPackagesUploadUrl(request)
    signed_url = response.upload_url

    with open(dependency_file_path, "rb") as fp:
        fp.seek(upload_part.offset)
        file_data = fp.read(upload_part.part_size)
        response = http.session().put(signed_url, data=file_data)
        if response.ok:
            e_tag = response.headers["ETag"]
            return S3UploadPart(part_number=upload_part.part_number, e_tag=e_tag, parent_upload_id=parent_upload_id)
        else:
            msg = f"Upload failed with status {response.status_code} and error {response.text}"
            raise ValueError(msg)


def _display_requirements(requirements_path: Optional[Path] = None, requirements_str: Optional[str] = None):
    """
    Display requirements from a requirements.txt file after removing hashes from each line, if exists.

    Args:
        requirements_path (Path): Path to the requirements file.
        requirements_str (str): Contents of a requirements.txt file
    """
    cleaned_lines = []
    if requirements_path is not None:
        with requirements_path.open("r") as file:
            cleaned_lines = [line.strip() for line in file.readlines()]
    elif requirements_str is not None:
        cleaned_lines = [line.strip() for line in requirements_str.split("\n")]

    # Skip hashes, comments, and empty lines.
    cleaned_lines = [
        line.rstrip("\\").strip()
        for line in cleaned_lines
        if line and not line.startswith("--hash") and not line.startswith("#")
    ]
    # Clean up extra flags from requirement lines
    cleaned_lines = [_clean_requirement_line(line) for line in cleaned_lines]
    printer.safe_print("\n".join(cleaned_lines))


def _search_environments_by_requirements(
    environments: List, package: str, version: Optional[str] = None
) -> List[Tuple]:
    """Search environments by their resolved requirements.

    Returns:
        List of tuples (environment, matched_packages) where matched_packages
        is a list of package lines that matched the search criteria.
    """
    matches = []

    for env in environments:
        if not env.resolved_requirements:
            continue

        matched_packages = []
        requirement_lines = [line.strip() for line in env.resolved_requirements.split("\n") if line.strip()]

        # Filter out hash lines, comment lines, and empty lines
        clean_lines = [
            line.rstrip("\\").strip()
            for line in requirement_lines
            if line and not line.startswith("#") and not line.startswith("--")
        ]

        for line in clean_lines:
            # Parse package name and version from line
            parsed_pkg = _parse_requirement_line(line)
            if not parsed_pkg:
                continue

            pkg_name, pkg_version = parsed_pkg

            # Check if package name matches (exact match, case insensitive)
            # Requirement parsing returns base package name already
            if pkg_name.lower() == package.lower():
                # If version constraint is specified, check it
                if version:
                    if _version_matches_constraint(pkg_version, version):
                        matched_packages.append(_clean_requirement_line(line))
                else:
                    matched_packages.append(_clean_requirement_line(line))

        if matched_packages:
            matches.append((env, matched_packages))

    return matches


def _clean_requirement_line(line: str) -> str:
    """Clean a requirement line by removing extra flags and options.

    Removes flags like:
    - --find-links
    - --index-url
    - --extra-index-url
    - --trusted-host
    - etc.

    Preserves URL-based requirements (@ file:// or @ https://).

    Returns the clean package requirement line.
    """
    if not line:
        return line

    # If this is a URL-based requirement, preserve the entire requirement
    if "@" in line and (" file://" in line or " https://" in line):
        # For URL-based requirements, only remove flags that come after the URL
        # The format is usually: "package @ url --flag value"
        parts = line.split()
        clean_parts = []
        skip_next = False

        for i, part in enumerate(parts):
            if skip_next:
                skip_next = False
                continue

            if part.startswith("--"):
                # This is a flag, check if the next part is its value
                if i + 1 < len(parts) and not parts[i + 1].startswith("--"):
                    skip_next = True
                continue
            else:
                clean_parts.append(part)

        return " ".join(clean_parts)

    # For standard requirements (package==version), use the original logic
    parts = line.split()
    if not parts:
        return line

    # Keep only the package requirement part (first part that doesn't start with --)
    clean_parts = []
    for part in parts:
        if part.startswith("--"):
            # Skip this flag and potentially the next part if it's the flag's value
            continue
        else:
            # This should be the package requirement
            clean_parts.append(part)
            break  # Only take the first non-flag part

    return " ".join(clean_parts) if clean_parts else line


def _parse_requirement_line(line: str) -> Optional[Tuple[str, str]]:
    """Parse a requirement line using packaging.Requirement and extract (name, version).

    - Returns base package name (extras removed)
    - For pinned specs (==), returns pinned version
    - For URL-based requirements (file:// or https://), extracts version from wheel filename if possible
    - Otherwise returns (name, "unknown")
    """
    if not line:
        return None

    try:
        req = Requirement(line)
        package_name = req.name

        # Prefer explicit pinned version when specified via '=='
        if req.specifier:
            for spec in req.specifier:
                if spec.operator == "==":
                    return package_name, spec.version

        # Handle direct references with URL; try to extract version from wheel filename
        if getattr(req, "url", None):
            parsed_url = urlparse(req.url)
            wheel_filename = os.path.basename(parsed_url.path)
            wheel_filename = unquote(wheel_filename)
            wheel_match = re.match(r"([\w.\-]+)-([\d.]+.*?)(-py\d|\.tar\.gz|\.zip|\.whl)", wheel_filename)
            if wheel_match:
                return package_name, wheel_match.group(2)
            return package_name, "unknown"

        # No specifier and no URL → unknown version in practice
        return package_name, "unknown"
    except Exception:
        return None


def _version_matches_constraint(version: str, constraint: str) -> bool:
    """Check if a version matches a constraint.

    Supports constraints like:
    - "1.2.3" (exact match)
    - ">=1.0" (greater than or equal)
    - "<2.0" (less than)
    - ">=1.0,<2.0" (range)
    """
    if not version or version == "unknown":
        return False

    try:
        from packaging import version as pkg_version
        from packaging.specifiers import SpecifierSet

        # Handle version constraints
        if any(op in constraint for op in [">=", "<=", ">", "<", "==", "!="]):
            # Multiple constraints separated by comma
            if "," in constraint:
                spec_set = SpecifierSet(constraint)
                return pkg_version.parse(version) in spec_set
            else:
                # Single constraint
                spec_set = SpecifierSet(constraint)
                return pkg_version.parse(version) in spec_set
        else:
            # Exact version match
            return pkg_version.parse(version) == pkg_version.parse(constraint)

    except Exception:
        # Fallback to string comparison if packaging module has issues
        if constraint.startswith(">="):
            constraint_version = constraint[2:].strip()
            return _simple_version_compare(version, constraint_version) >= 0
        elif constraint.startswith("<="):
            constraint_version = constraint[2:].strip()
            return _simple_version_compare(version, constraint_version) <= 0
        elif constraint.startswith(">"):
            constraint_version = constraint[1:].strip()
            return _simple_version_compare(version, constraint_version) > 0
        elif constraint.startswith("<"):
            constraint_version = constraint[1:].strip()
            return _simple_version_compare(version, constraint_version) < 0
        elif constraint.startswith("=="):
            constraint_version = constraint[2:].strip()
            return version == constraint_version
        else:
            # Exact match
            return version == constraint


def _simple_version_compare(v1: str, v2: str) -> int:
    """Simple version comparison fallback."""

    def normalize_version(v):
        return [int(x) for x in re.sub(r"[^\d.]", "", v).split(".") if x.isdigit()]

    v1_parts = normalize_version(v1)
    v2_parts = normalize_version(v2)

    # Pad with zeros to make equal length
    max_len = max(len(v1_parts), len(v2_parts))
    v1_parts.extend([0] * (max_len - len(v1_parts)))
    v2_parts.extend([0] * (max_len - len(v2_parts)))

    for a, b in zip(v1_parts, v2_parts):
        if a < b:
            return -1
        elif a > b:
            return 1
    return 0


def _display_search_results(matches: List[Tuple]):
    """Display search results in a formatted table."""
    headings = ["Id", "Name", "Type", "Status", "Created At", "Matched Packages"]

    rows = []
    for env, matched_packages in matches:
        # Show all matched packages (should be few since we're doing exact matching)
        matched_summary = "\n".join(matched_packages)

        row = (
            env.id,
            env.name,
            RemoteComputeType.Name(env.type).split("_")[-1],
            RemoteEnvironmentStatus.Name(env.status).split("_")[-1],
            timestamp_to_string(env.created_at),
            matched_summary,
        )
        rows.append(row)

    display_table(headings, rows)
