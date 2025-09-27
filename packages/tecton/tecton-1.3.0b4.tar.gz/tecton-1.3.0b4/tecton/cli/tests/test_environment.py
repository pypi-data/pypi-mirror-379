import os
from dataclasses import dataclass
from typing import List

import pytest

from tecton.cli.environment import UploadPart
from tecton.cli.environment import _get_pkg_to_version
from tecton.cli.environment import _run_dependency_resolution
from tecton.cli.environment import _search_environments_by_requirements
from tecton.cli.environment import _validate_input_requirements
from tecton.cli.environment import get_upload_parts
from tecton.cli.environment_utils import is_valid_environment_name
from tecton.cli.upload_utils import DEFAULT_UPLOAD_PART_SIZE_MB


ERROR_INPUT_REQUIREMENTS_TEXT = """
urllib3<1.27
tecton==1.1.0b6
"""

INPUT_REQUIREMENTS_TEXT = """
# THIS IS A MESS
# This is an implicit value, here for clarity
--index-url https://pypi.python.org/simple/

# pypika @ https://s3.us-west-2.amazonaws.com/tecton.ai.public/python/PyPika-0.48.9-py2.py3-none-any.whl
xformers==0.0.28.post1
# tecton[rift-materialization] @ file:///Users/vitaly/dev/tecton/bazel-bin/sdk/pypi/tecton-99.99.99-py3-none-any.whl # hello
tecton-runtime==1.0.0

# pydantic<2
# setuptools<70
urllib3<1.27

# protobuf<=4.25.3 # hi
tecton[rift-materialization]==1.1.0b6
"""

RESOLVED_REQUIREMENTS_TEXT = """
--index-url https://pypi.python.org/simple/
--find-links https://s3.us-west-2.amazonaws.com/tecton.ai.public/python/index.html

deltalake==0.18.2
    # via tecton
    # from https://pypi.python.org/simple/
tecton[rift-materialization] @ file:///Users/vitaly/dev/tecton/bazel-bin/sdk/pypi/tecton-99.99.99-py3-none-any.whl
    # via -r requirements.txt
tecton-runtime==1.0.0
    # via -r requirements.txt
    # from https://pypi.python.org/simple/
"""

RESOLVED_REQUIREMENTS_TEXT_WITH_MULTI_EXTRAS = """
--index-url https://pypi.python.org/simple/

tecton[rift-materialization,ml-extras]==1.3.4
"""


SAMPLE_LOCK_JSON = {
    "locked_resolves": [
        {
            "locked_requirements": [
                {
                    "project_name": "attrs",
                    "requires_dists": [
                        "attrs[tests-mypy]; extra == 'tests-no-zope'",
                        "hypothesis; extra == 'tests-no-zope'",
                    ],
                    "version": "23.2.0",
                },
                {"project_name": "boto3", "requires_dists": ["botocore<1.35.0,>=1.34.87"], "version": "1.34.87"},
                {"project_name": "pytest", "requires_dists": [], "version": "8.1.1"},
            ]
        }
    ],
    "requirements": ["attrs==23.2.0", "boto3==1.34.87", "pytest"],
}


@pytest.fixture
def uv_binary_setup(tmp_path):
    import importlib.metadata
    from importlib.util import find_spec

    version = importlib.metadata.version("uv")
    base_dir = os.path.dirname(os.path.dirname(find_spec("uv").origin))
    new_path = os.path.join(base_dir, f"uv-{version}.data/scripts")
    # set this up because `uv` via @pip does not unpack binaries in discoverable location
    if os.path.exists(new_path):
        os.environ["UV_INSTALL_DIR"] = new_path


@pytest.fixture
def input_requirements_file(tmp_path):
    requirements_path = tmp_path / "requirements.txt"
    requirements_path.write_text(INPUT_REQUIREMENTS_TEXT)
    return requirements_path


@pytest.fixture
def error_input_requirements_file(tmp_path):
    requirements_path = tmp_path / "resolved.txt"
    requirements_path.write_text(ERROR_INPUT_REQUIREMENTS_TEXT)
    return requirements_path


@pytest.fixture
def resolved_requirements_file(tmp_path):
    requirements_path = tmp_path / "resolved.txt"
    requirements_path.write_text(RESOLVED_REQUIREMENTS_TEXT)
    return requirements_path


@pytest.fixture
def resolved_requirements_with_multi_extras_file(tmp_path):
    requirements_path = tmp_path / "resolved_multi_extras.txt"
    requirements_path.write_text(RESOLVED_REQUIREMENTS_TEXT_WITH_MULTI_EXTRAS)
    return requirements_path


@pytest.fixture
def input_requirements_with_multi_extras_file(tmp_path):
    path = tmp_path / "requirements_multi_extras.txt"
    path.write_text("tecton[rift-materialization,ml-extras]==1.2.3\n")
    return path


@dataclass
class FileSplit__TestCase:
    name: str
    file_size: int
    expected_parts: List[UploadPart]


FILE_SPLIT_TEST_CASES = [
    FileSplit__TestCase(
        name="single_file",
        file_size=DEFAULT_UPLOAD_PART_SIZE_MB * 1024 * 1024 - 1,
        expected_parts=[UploadPart(part_number=1, offset=0, part_size=DEFAULT_UPLOAD_PART_SIZE_MB * 1024 * 1024 - 1)],
    ),
    FileSplit__TestCase(
        name="exact_multiple_parts",
        file_size=DEFAULT_UPLOAD_PART_SIZE_MB * 1024 * 1024 * 5,
        expected_parts=[
            UploadPart(
                part_number=i,
                offset=(i - 1) * DEFAULT_UPLOAD_PART_SIZE_MB * 1024 * 1024,
                part_size=DEFAULT_UPLOAD_PART_SIZE_MB * 1024 * 1024,
            )
            for i in range(1, 6)
        ],
    ),
    FileSplit__TestCase(
        name="multiple_parts_with_last_part_smaller",
        file_size=(DEFAULT_UPLOAD_PART_SIZE_MB * 1024 * 1024 * 2) + (DEFAULT_UPLOAD_PART_SIZE_MB * 1024 * 1024 // 2),
        expected_parts=[
            UploadPart(part_number=1, offset=0, part_size=DEFAULT_UPLOAD_PART_SIZE_MB * 1024 * 1024),
            UploadPart(
                part_number=2,
                offset=DEFAULT_UPLOAD_PART_SIZE_MB * 1024 * 1024,
                part_size=DEFAULT_UPLOAD_PART_SIZE_MB * 1024 * 1024,
            ),
            UploadPart(
                part_number=3,
                offset=2 * DEFAULT_UPLOAD_PART_SIZE_MB * 1024 * 1024,
                part_size=DEFAULT_UPLOAD_PART_SIZE_MB * 1024 * 1024 // 2,
            ),
        ],
    ),
    FileSplit__TestCase(
        name="zero_size_file",
        file_size=0,
        expected_parts=[],
    ),
]


@pytest.mark.parametrize("test_case", FILE_SPLIT_TEST_CASES, ids=[tc.name for tc in FILE_SPLIT_TEST_CASES])
def test_get_upload_parts(test_case):
    parts = get_upload_parts(test_case.file_size)
    assert len(parts) == len(test_case.expected_parts)
    for part, expected_part in zip(parts, test_case.expected_parts):
        assert part.part_size == expected_part.part_size
        assert part.part_number == expected_part.part_number
        assert part.offset == expected_part.offset


@pytest.mark.parametrize(
    "name, expected",
    [
        ("env123", True),
        ("env_123", True),
        ("ENV-123", True),
        ("env*123", False),
        ("env?123", False),
        ("env!123", False),
        ("", False),
        ("env 123", False),
        ("env_01234567890123456789001234567890012345678900123456789001234567890", False),
    ],
)
def test_environments(name, expected):
    assert is_valid_environment_name(name) == expected


def test_error_requirements_resolution(error_input_requirements_file, tmp_path):
    # exists because requirements does not have any supporting tecton libraries
    with pytest.raises(SystemExit) as e:
        _run_dependency_resolution(error_input_requirements_file, tmp_path, python_version="3.9")
    assert e.type == SystemExit
    assert e.value.code == 1


def test_get_tecton_versions_from_resolved(resolved_requirements_file):
    tecton_pkg_to_version = _get_pkg_to_version(
        resolved_requirements_file, packages=["tecton[rift-materialization]", "tecton-runtime", "deltalake"]
    )
    tecton_runtime_version = tecton_pkg_to_version.get("tecton-runtime")
    tecton_rift_version = tecton_pkg_to_version.get("tecton[rift-materialization]")
    deltalake_version = tecton_pkg_to_version.get("deltalake")

    assert tecton_runtime_version == "1.0.0"
    assert tecton_rift_version == "99.99.99"
    assert deltalake_version == "0.18.2"


def test_search_matches_url_and_exact():
    class Env:
        def __init__(self, id, name, resolved_requirements):
            self.id = id
            self.name = name
            self.resolved_requirements = resolved_requirements

    envs = [
        Env("e1", "env1", RESOLVED_REQUIREMENTS_TEXT),
        Env("e2", "env2", "requests==2.32.4\ntecton-runtime==0.9.0\n"),
    ]

    # tecton should match tecton[rift-materialization] @ file://...
    matches = _search_environments_by_requirements(envs, package="tecton", version=None)
    assert len(matches) == 1
    env, pkgs = matches[0]
    assert env.id == "e1"
    assert any("tecton[rift-materialization] @ file://" in p for p in pkgs)

    # exact name tecton-runtime should match in both envs when no version constraint
    matches = _search_environments_by_requirements(envs, package="tecton-runtime", version=None)
    assert len(matches) == 2


def test_search_version_constraints():
    class Env:
        def __init__(self, id, name, resolved_requirements):
            self.id = id
            self.name = name
            self.resolved_requirements = resolved_requirements

    envs = [Env("e1", "env1", RESOLVED_REQUIREMENTS_TEXT)]

    # >=1.0,<2.0 should match tecton-runtime==1.0.0
    matches = _search_environments_by_requirements(envs, package="tecton-runtime", version=">=1.0,<2.0")
    assert len(matches) == 1

    # <1.0 should not match tecton-runtime==1.0.0
    matches = _search_environments_by_requirements(envs, package="tecton-runtime", version="<1.0")
    assert len(matches) == 0


def test_get_tecton_versions_from_resolved_with_multi_extras(resolved_requirements_with_multi_extras_file):
    versions = _get_pkg_to_version(
        resolved_requirements_with_multi_extras_file, packages=["tecton[rift-materialization]"]
    )
    assert versions.get("tecton[rift-materialization]") == "1.3.4"


def test_validate_input_requirements_accepts_multiple_extras(input_requirements_with_multi_extras_file):
    # Should not raise SystemExit
    _validate_input_requirements(input_requirements_with_multi_extras_file)


def test_validate_input_requirements_accepts_mixed_sources(tmp_path):
    # Includes: PyPI pins, local wheel file (file URL), and HTTP(S) wheel URL.
    # Also includes a required Tecton supporting package to pass our validation.
    local_wheel = tmp_path / "my_local_pkg-1.0.0-py3-none-any.whl"
    reqs = tmp_path / "requirements.txt"
    reqs.write_text(
        f"\n"  # leading newline intentionally
        f"fuzzywuzzy==0.18.0\n"
        f"tecton-runtime==1.2.4\n"
        f"tecton[rift-materialization,snowflake]\n"
        f"file://{local_wheel}\n"
        f"https://s3.amazonaws.com/example-bucket/wheels/example_pkg-0.1.0-py3-none-any.whl\n"
    )

    # Should not raise SystemExit
    _validate_input_requirements(reqs)
