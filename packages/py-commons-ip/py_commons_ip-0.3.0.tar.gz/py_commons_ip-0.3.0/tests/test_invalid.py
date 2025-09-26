from py_commons_ip import validate
from pathlib import Path


def test_with_non_existant_path():
    succes, report = validate(Path("./path-that-does-not-exists"), "2.2.0")

    print(report)
    assert not succes


def test_with_invalid_sip():
    succes, report = validate(
        Path("tests/sip-examples/1.0/basic_deec5d89-3024-4cbd-afcd-e18af4ad33ec/data"),
        "2.2.0",
    )

    print(report)
    assert not succes
