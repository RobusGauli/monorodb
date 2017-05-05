import os
import sys


import six
import unicodedata
import collections 
from concurrent.futures import Future
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

class NotFoundError(Exception):

    def __init__(self, val):
        self.val = val
        super().__init__(val)


class Cache(dict):

    def __getattr__(self, key):
        return self.get(key, '')
    def __setattr__(self, key, val):
        self[key] = val
    
    