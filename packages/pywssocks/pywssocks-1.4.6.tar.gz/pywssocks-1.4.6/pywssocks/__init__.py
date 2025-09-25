__version__ = "1.4.6"

import importlib as _i
import typing as _t

if _t.TYPE_CHECKING:
    from .server import WSSocksServer
    from .client import WSSocksClient
    from .common import PortPool

MENU = {
    ".server": ["WSSocksServer"],
    ".client": ["WSSocksClient"],
    ".common": ["PortPool"],
}


def __getattr__(spec: str):
    for module, specs in MENU.items():
        if isinstance(specs, dict):
            for s, t in specs.items():
                if s == spec:
                    m = _i.import_module(module, package=__name__)
                    return getattr(m, t or s)
        else:
            if spec in specs:
                m = _i.import_module(module, package=__name__)
                return getattr(m, spec)
    else:
        try:
            m = _i.import_module(f".{spec}", package=__name__)
            return m
        except ImportError:
            raise AttributeError(
                f"module '{__name__}' has no attribute '{spec}'"
            ) from None
