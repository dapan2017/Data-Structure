# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 20:45:09 2018

@author: ustbp
"""

class Stack():
    def __init__(self,iterator=None):
        if iterator is None:
            self.stack = []
        else:
            self.stack = []
            self._construct(iterator)
        
    def _construct(self,iterator):
        for i in iterator:
            self.stack.append(i)

    def pop(self):
        if len(self.stack)== 0:
            raise ValueError
        return self.stack.pop()
        
    def push(self,val):
        self.stack.append(val)
        
    def peek(self):
        return self.stack[-1]
    
    def __repr__(self):
        res = ''
        for i in self.stack:
            res+=str(i)+' '
        return res