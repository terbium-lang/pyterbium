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


# noinspection PyShadowingBuiltins
class Object:
    def __init__(self, id: int, type: Object, attrs: Dict[str, Object] = None) -> None:
        self.__id: int = id
        self.type: Object = type
        self.internals: ObjectInternals = ObjectInternals(self, attrs=attrs)

    def __repr__(self) -> str:
        return f'<Object type={self.type} id={self.id}>'

    @property
    def id(self) -> int:
        return self.__id
