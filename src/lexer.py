import re
from rply import LexerGenerator as _BaseGen


class LexerGenerator:
    def __init__(self) -> None:
        self._lg: _BaseGen = _BaseGen()
        self.inject()

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}>'

    def add(self, name: str, pattern: str, *, flags: int = 0) -> None:
        self._lg.add(name, pattern, flags)

    def ignore(self, pattern: str, *, flags: int = 0) -> None:
        self._lg.ignore(pattern, flags)

    def inject(self) -> None:
        self.ignore(r'\s+')
        self.ignore(r'//.*')
        self.ignore(r'/\*.*\*/', flags=re.S)

        self.add('STRING', r'''(['"])[^\1]*(?<!\\)\1''')

        # Keywords, sorted by length to prevent conflicts
        self.add('CONTINUE', 'continue')
        self.add('REQUIRE', 'require')
        self.add('PRIVATE', 'private')
        self.add('PUBLIC', 'public')
        self.add('OBJECT', 'object')
        self.add('RETURN', 'return')
        self.add('STATIC', 'static')
        self.add('BREAK', 'break')
        self.add('CLASS', 'class')
        self.add('WHERE', 'where')
        self.add('CONST', 'const')
        self.add('IMMUT', 'immut')
        self.add('WHILE', 'while')
        self.add('YIELD', 'yield')
        self.add('ELSE', 'else')
        self.add('FUNC', 'func')
        self.add('WITH', 'with')
        self.add('FROM', 'from')
        self.add('CAST', 'cast')
        self.add('FOR', 'for')
        self.add('GET', 'get')
        self.add('SET', 'set')
        self.add('IF', 'if')
        self.add('IN', 'in')
        self.add('OP', 'op')
        self.add('AS', 'as')

        # Async stuff, maybe later
        # self.add('ASYNC', 'async')
        # self.add('AWAIT', 'await')

        self.add('LBRACE', r'\{')
        self.add('RBRACE', r'\}')

        self.add('LPAREN', r'\(')
        self.add('RPAREN', r'\)')

        self.add('LBRACK', r'\[')
        self.add('RBRACK', r'\]')

        self.add('LANGLE', '<')
        self.add('RANGLE', '>')

        self.add('FLOAT_LITERAL', r'([1-9][0-9]*|0)\.[0-9]*|[0-9]*\.[0-9]+')
        self.add('INTEGER_LITERAL', '[1-9][0-9]*|0')
        self.add('NAME', '[a-zA-Z_][a-zA-Z0-9_]*')

        self.add('LAMBDA', '->')

        self.add('OPTCHAIN', r'\?\.')
        self.add('QUESTION', r'\?')

        self.add('DOT', r'\.')
        self.add('COMMA', ',')
        self.add('CAST', '::')
        self.add('COLON', ':')
        self.add('SEMICOLON', ';')

        self.add('EQ', '==')
        self.add('NE', '!=')

        self.add('WALRUS', ':=')  # ew
        self.add('DECL', '=')
        self.add('NOT', '!')

        self.add('INCR', r'\+\+')
        self.add('DECR', r'--')

        self.add('ADD', r'\+')
        self.add('SUB', '-')
        self.add('POW', r'\*\*')
        self.add('MUL', r'\*')
        self.add('DIV', '/')
