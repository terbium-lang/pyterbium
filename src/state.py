from .object import Object, Reference
from typing import Dict


class State:
    def __init__(self) -> None:
        self._increment: int = -1
        self._lookup: Dict[int, Object] = {}
        self.builtins: Dict[str, Object] = {}
        self.globals: Dict[str, Object] = {}
        self.allocate_builtins()

    def _resolve_import(self, spec: str) -> str:
        ...

    def allocate(self, obj: Object) -> Object:
        self._increment += 1
        self._lookup[self._increment] = obj
        obj._put_id(self._increment)
        return obj

    def deallocate(self, obj: Object) -> int:
        store = obj.id
        obj._deallocate()
        del self._lookup[obj.id]
        return store

    def lookup(self, id: int, /) -> Object:
        return self._lookup[id]

    def allocate_builtins(self) -> None:
        self.builtins['Type'] = Type = self.allocate(Object(self, Reference(0), const=True))
        self.builtins['int'] = self.allocate(Object(self, Type, const=True))
