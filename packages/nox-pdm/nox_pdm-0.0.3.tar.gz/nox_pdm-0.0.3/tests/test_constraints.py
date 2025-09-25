from importlib.metadata import version


def test_constraints_versions_match():
    # TODO: read expected versions using tomli and pdm.lock

    assert version("pytest_icdiff") == "0.8"

    assert version("urllib3") == "2.1.0"
