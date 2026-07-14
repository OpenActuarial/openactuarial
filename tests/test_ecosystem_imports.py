"""The meta-package's one contract: the pinned ecosystem resolves and imports."""
import importlib

import openactuarial

PACKAGES = ("actuarialpy", "experiencestudies", "projectionmodels",
            "ratingmodels", "reservingmodels", "lossmodels", "extremeloss", "risksim")


def test_every_pinned_package_imports():
    for name in PACKAGES:
        assert importlib.import_module(name).__name__ == name


def test_meta_reports_its_version():
    assert openactuarial.__version__
