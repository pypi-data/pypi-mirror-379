# version handling
try:
    # setuptools_scm will generate this file during build when write_to is configured
    from ._version import version as __version__
except Exception:
    # fallback: try importlib.metadata (works when package is installed)
    try:
        from importlib.metadata import version, PackageNotFoundError
        __version__ = version("matrixutils_example_pkg")
    except Exception:
        __version__ = "0.0.0"