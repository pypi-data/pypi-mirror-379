"""Sphinx extension to fix relative links in documentation."""

try:
    from ._version import version as __version__
except ImportError:
    # 2) Fallback to installed package metadata
    try:
        from importlib.metadata import PackageNotFoundError, version
    except ImportError:
        # Very old Python or exotic environment
        __version__ = "0.0.0"
    else:
        try:
            __version__ = version("sphinx_linkfix")
        except PackageNotFoundError:
            __version__ = "0.0.0"
        finally:
            # Avoid leaking names into the package namespace
            del version
            del PackageNotFoundError

# Expose the setup function for Sphinx extension
from .extension import setup

__all__ = ["__version__", "setup"]
