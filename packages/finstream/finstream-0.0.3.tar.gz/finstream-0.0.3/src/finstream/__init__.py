"""finstream Python SDK."""

from ._version import __version__


def version() -> str:
    return __version__


__all__ = ["version", "__version__"]


