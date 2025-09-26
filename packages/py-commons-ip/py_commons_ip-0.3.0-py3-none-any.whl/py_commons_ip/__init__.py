from typing import Literal
from pathlib import Path
import importlib.resources
import subprocess
import json


resources = importlib.resources.files("py_commons_ip.resources")
cli_jar = resources.joinpath("commons-ip2-cli.jar")

Version = Literal["2.2.0"]


def validate(unzipped_path: Path, version: Version) -> tuple[bool, str]:
    """
    Validate an unzipped SIP making use of the commons-IP validator

    Args:
        The folder pointing to an unzipped SIP.

    Returns:
        tuple: A tuple containing:
          - bool: Whether the SIP is valid.
          - str: The full JSON report in string format.

    """

    result = subprocess.run(
        [
            "java",
            "-jar",
            str(cli_jar),
            "validate",
            "-i",
            str(unzipped_path),
            "--specification-version",
            "2.2.0",
        ],
        capture_output=True,
    )

    if result.stdout is None:
        print("Error while running commons-ip cli subprocess")
        exit(1)

    output = result.stdout.decode()
    is_valid = json.loads(output)["summary"]["result"] == "VALID"

    return is_valid, output
