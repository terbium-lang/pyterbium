from .ast import *
from .lexer import LexerGenerator
from .state import State

from rply import ParserGenerator, Token

from typing import List

ProdT = List[Token]


lg: LexerGenerator = LexerGenerator()
pg: ParserGenerator = ParserGenerator(
    [rule.name for rule in lg.rules],
    precedence=[
        ('right', ['UMINUS']),
        ('left', ['ADD', 'SUB']),
        ('left', ['MUL', 'DIV', 'MOD']),
        ('right', ['POW'])
    ]
)


@pg.production('expr : INTEGER')
def program(_: State, p: ProdT) -> ProdT:
    return Integer(int(p[0]))
