from importlib import import_module


def test_package_can_be_imported() -> None:
    package = import_module("gbdj")
    assert package.__doc__
