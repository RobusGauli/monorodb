import os
import sys
from lexer import (
    Lexer,
    Token,
    MSyntaxError
)

from protocol import (
    Protocol,
    MonoroMessage
)

from collections import namedtuple

KeyVal = namedtuple('KeyVal', ['key', 'val'])

class Parser(object):
    def __init__(self, text):
        lexer = Lexer(text)
        self.token = lexer.tokens()

    def parse(self):
        if self.token[0] == 'CREATE':
            return MonoroMessage('CREATE', self.token[1].val)

        if self.token[0] == 'GET':
            return MonoroMessage('GET', self.token[1].val)

        if self.token[0] == 'SET':
            return MonoroMessage('SET', KeyVal(self.token[1][0].val, self.token[1][1].val))


        