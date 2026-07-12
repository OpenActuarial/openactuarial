"""openactuarial: one install for the whole OpenActuarial ecosystem."""
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("openactuarial")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "0+unknown"

__all__ = ["__version__"]
