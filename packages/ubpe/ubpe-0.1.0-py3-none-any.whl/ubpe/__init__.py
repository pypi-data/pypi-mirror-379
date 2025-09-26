__version__ = "0.1.0"

try:
    from ubpe_native import UBPE, UBPEClassic # type: ignore
except ImportError:
    raise Exception(
        "Implementation package was not found. Make sure that you are installing the package with optional dependency: `pip install ubpe[native]`"
    )

__all__ = ["UBPEClassic", "UBPE"]
