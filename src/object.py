from __future__ import annotations

from typing import Dict, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from .state import State

Function = None  # AST, Placeholder


class Reference:
    def __init__(self, id: int, /) -> None:
        self.id: int = id


class ObjectInternals:
    def __init__(
        self,
        obj: Object,
        *,
        attrs: Dict[str, Object] = None,
        immut: bool = False,
        const: bool = False
    ) -> None:
        self.object: Object = obj
        self.attrs: Dict[str, Object] = attrs or {}

        self.operators: Dict[str, Function] = {}
        self.casts: Dict[str, Function] = {}

        self.getters: Dict[str, Function] = {}
        self.setters: Dict[str, Function] = {}

        self.mutable: bool = not immut
        self.constant: bool = const

    def get_operation(self, name: str, /) -> Function:
        return self.operators.get(name)


# noinspection PyShadowingBuiltins
class Object:
    def __init__(
        self,
        state: State,
        type: Union[Object, Reference],
        attrs: Dict[str, Object] = None,
        *,
        immut: bool = False,
        const: bool = False
    ) -> None:
        self.__id: int = None
        self.__type_ref: int = type.id

        self.state: State = state
        self.internals: ObjectInternals = ObjectInternals(
            self,
            attrs=attrs,
            immut=immut,
            const=const
        )

    def __repr__(self) -> str:
        return f'<Object type={self.type} id={self.id}>'

    def _put_id(self, id: int) -> None:
        self.__id = id

    def _deallocate(self) -> None:
        self.__id = None

    @property
    def id(self) -> int:
        if self.__id is None:
            raise ValueError('object not properly allocated')
        return self.__id

    @property
    def type(self) -> Object:
        return self.state.lookup(self.__type_ref)
