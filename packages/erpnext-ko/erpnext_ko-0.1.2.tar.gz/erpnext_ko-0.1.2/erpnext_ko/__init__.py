from importlib.metadata import version, PackageNotFoundError

def __version__() -> str:
    try:
        return version("erpnext-ko")
    except PackageNotFoundError:  # pragma: no cover - during development
        return "0.0.0"
