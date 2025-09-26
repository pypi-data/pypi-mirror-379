from .symdb import (
    Language,
    SymbolType,
    Symbol,
    Location,
    ImmediateSymbolDatabase,
    LazySymbolDatabase,
    AsyncSymbolDatabase,
    AsyncResult,
)

__version__ = "2.0.0"
__version_info__ = tuple(int(i) for i in __version__.split('.'))

__all__ = [
    "Language",
    "SymbolType",
    "Symbol",
    "Location",
    "ImmediateSymbolDatabase",
    "LazySymbolDatabase",
    "AsyncSymbolDatabase",
    "AsyncResult",
    "SymbolDatabase",
]
