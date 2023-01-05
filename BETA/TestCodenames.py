#!/usr/bin/env python3
#
#TestCodenames.py
#
#
#
#

import unittest
from CodeNames import *
import MyDictionary
import FIFO
import copy
import autocomplete

class TestCodenames(unittest.TestCase):

    def test__init__(self):

        c = CodeNames()
        
        #Is c of the CodeNames class?
        self.assertIsInstance(c, CodeNames)

        #Does c.names create a custom dictionary?
        self.assertIs(type(c.names), MyDictionary.MyDictionary)

        #Does c.vectors create a python dictionary
        self.assertIs(type(c.vectors), dict)

        #Does c.queue create a custom queue
        self.assertIs(type(c.queue), FIFO.FIFO)
        
        #Does c.queue create a custom queue
        self.assertIs(type(c.trie), autocomplete.Trie)        
        

    def test_Immutability(self):

        c = CodeNames()

        #change the dictionary
        MyDict = MyDictionary.MyDictionary(10)
        flag = False
        try:
            c.names = MyDict
        except AttributeError:
            flag = True

        self.assertTrue(flag)


        #change the vectors
        newvect = {}
        flag = False
        try:
            c.vectors = newvect
        except AttributeError:
            flag = True

        self.assertTrue(flag)    

        
        #change the queue
        newq = FIFO.FIFO()
        flag = False
        try:
            c.queue = newq
        except AttributeError:
            flag = True

        self.assertTrue(flag) 
        
        
        #change the trie
        newq = autocomplete.Trie()
        flag = False
        try:
            c.trie = newq
        except AttributeError:
            flag = True

        self.assertTrue(flag)         


    def test__copy__(self):

        c = CodeNames()
        c2 = copy.copy(c)
        self.assertNotEqual(c, c2)        


    def test__deepcopy__(self):

        c = CodeNames()
        c2 = copy.deepcopy(c)
        self.assertNotEqual(c, c2) 


    def test__eq__(self):

        c = CodeNames()
        c2 = copy.copy(c)
        c_id = id(c)
        c2_id = id(c2)
        self.assertNotEqual(c_id, c2_id)        
              
    def test_hash(self):

        c = CodeNames() 
        result = hash(c)

        c1 = CodeNames() 
        expected = hash(c1)

        self.assertNotEqual(result, expected)
    
#    def test__ne__(self):
#       Taken care of with the test for deep copy and copy

#************* automated tests run below
#
if __name__ == "__main__":
    unittest.main(exit=False)
       