from rply import ParserGenerator, Token
from .state import State

from typing import List

from .lexer import LexerGenerator

T = List[Token]

parser = ParserGenerator([l.name for l in LexerGenerator()._lg.rules])

@parser.production('program : statements')
def program(state: State, p: T) -> T:
    return p[0]

@parser.production('statements : statement statements')
def statements(state: State, p: T) -> T:
    return p[0] + p[1]