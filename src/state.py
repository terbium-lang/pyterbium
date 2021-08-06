from .object import Object
from typing import Dict


class State:
    def __init__(self) -> None:
        self._increment: int = 0
        self._lookup: Dict[int, Object] = {}
        self.builtins: Dict[str, Object] = {}
        self.globals: Dict[str, Object] = {}

    def _resolve_import(self, spec: str) -> str:
        ...
