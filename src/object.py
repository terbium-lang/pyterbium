from __future__ import annotations

from typing import Dict

Function = None  # AST, Placeholder


class ObjectInternals:
    def __init__(self, obj: Object, *, attrs: Dict[str, Object] = None) -> None:
        self.object: Object = obj
        self.attrs: Dict[str, Object] = attrs or {}

        self.operators: Dict[str, Function] = {}
        self.casts: Dict[str, Function] = {}

        self.getters: Dict[str, Function] = {}
        self.setters: Dict[str, Function] = {}

    def get_operation(self, name: str, /) -> Function:
        return self.operators.get(name)


class Object:
    def __init__(self, id: int, attrs: Dict[str, Object] = None) -> None:
        self.__id: int = id
        self.internals: ObjectInternals = ObjectInternals(self, attrs=attrs)

    @property
    def id(self) -> int:
        return self.__id
