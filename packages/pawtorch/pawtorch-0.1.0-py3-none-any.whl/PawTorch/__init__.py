# pawtorch/__init__.py
from ._patch import activate as _activate
_activate()

__all__ = ["_activate"]
