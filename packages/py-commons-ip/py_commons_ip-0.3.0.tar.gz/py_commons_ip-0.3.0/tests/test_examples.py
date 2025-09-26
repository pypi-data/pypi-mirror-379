from py_commons_ip import validate
from pathlib import Path

import pytest

sip_paths = Path("tests/sip-examples/2.1").iterdir()
unzipped_paths = [next(path.iterdir()) for path in sip_paths]


@pytest.mark.parametrize("unzipped_path", unzipped_paths)
def test_examples_2_1(unzipped_path: Path):
    succes, report = validate(unzipped_path, "2.2.0")

    print(report)
    assert succes


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python -m tests.test_examples PATH")
        exit(1)

    test_examples_2_1(Path(sys.argv[1]))
