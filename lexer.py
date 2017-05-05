

import os
import re

class TokenType:
    CREATE = 'create'
    GET = 'get'
    SET = 'set'
    TABLE_NAME = 'tablename'
    KEY = 'key'
    VAL = 'val'

class Token(object):
    def __init__(self, val, _type):
        self.val = val
        self._type = _type
    
    def __repr__(self):
        return '<Token %r, %r>' % (self.val, self._type)


    
class MSyntaxError(Exception):
    def __init__(self, val):
        self.val = val
        super().__init__(val)

    
class Lexer(object):
    
    def __init__(self, text):
        self.text = text
        self.num_of_tokens = 0
        self.syntax = self.text.split()
        
    def tokens(self):
        if self.syntax[0] == 'CREATE':
            try:
                token = Token(self.syntax[1], TokenType.TABLE_NAME)
            except IndexError as e:
                raise MSyntaxError('Table name not specified')
            else:
                return 'CREATE', token
        if self.syntax[0] == 'GET':
            try:
                token = Token(self.syntax[1], TokenType.GET)
            except IndexError as e:
                raise MSyntaxError('Key not specified')
            else:
                return 'GET', token
        if self.syntax[0] == 'SET':
            try: 
                token = (Token(self.syntax[1], TokenType.KEY), Token(self.syntax[2], TokenType.VAL))
            except IndexError as e:
                raise MSyntaxError('Key/Val not specified')
            else:
                return 'SET', token
        raise MSyntaxError('Syntax Error')


        
