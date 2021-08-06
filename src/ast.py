from abc import ABC, abstractmethod
from rply.token import BaseBox

__all__ = (
    'Integer',
    'Float'
)


class AstToken(BaseBox, ABC):
    @abstractmethod
    def getval(self) -> int:
        raise NotImplementedError


class Integer(AstToken):
    def __init__(self, value: int, /) -> None:
        self.value: int = value

    def getval(self) -> int:
        return self.value


class Float(AstToken):
    def __init__(self, value: float, /) -> None:
        self.value: float = value

    def getval(self) -> float:
        return self.value
