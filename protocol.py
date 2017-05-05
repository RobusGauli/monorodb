from lexer import (
    MSyntaxError,
    Lexer,
    TokenType
)


class Protocol(object):
    CREATE = 'create'
    GET = 'get'
    SET = 'set'

class MonoroMessage(object):
    def __init__(self, proto, val):
        self.proto = proto
        self.val = val

        
      