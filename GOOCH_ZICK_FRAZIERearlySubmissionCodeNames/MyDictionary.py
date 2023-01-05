#Stack
#
# CS3021 LL Project
#
# winter 2019
# last updated: 04 Jan 2019
#
import LinkedList 
import math

def checkNumeric(value):
    if  not isinstance(value, int) and not isinstance(value, float):
        raise RuntimeError(value + ' is not a number')
    return value


def checkPositive(value):
    value = checkNumeric(value)
    if value <= 0:
        raise RuntimeError(str(value) + ' is not a positive value')
    return value

class MyDictionary(object):
    ''' MyDictionary Class.
    
        MyDictionary class contains and array of bins containing LinkedLists. Each 
        LinkedList contains <key,value> pairs. MyDictionary can insert and remove
        <key,value> pairs; utput list of items, keys, or values; get value for given
        key; update our dictionary with the values from a secondary dictionary; 
        return number of <key,value> pairs; and output all items to a string.
        
    '''
    
            
    def __init__(self, num):
        ''' Constructor.  Creates an array of bins according to user input.'''
        if checkNumeric(num) and checkPositive(num):
            self.__numBins = math.ceil(int(num)*1.43)
            self.__bins = []
            for i in range(0,self.__numBins):
                self.__bins.append(LinkedList.LinkedList())
        return
        
    @property
    def numBins(self):
        ''' Number of bins in the dictionary. '''
        return self.__numBins
    
    @property
    def bins(self):
        ''' Array of bins in the dictionary. '''
        return self.__bins

    def items(self):
        ''' Returns a list of all <key,value> pairs in the dictionary. '''
        items = []
        for x in self.bins:
            i = 0
            while x.read(i):
                items.append(x.read(i))
                i += 1
        return items
        
    def list(self):
        ''' Returns a list of all <key,value> pairs in the dictionary.'''
        return self.items()

    def __len__(self):
        ''' Calculates and returns the number of <key,value> pairs in the dictionary. '''
        total = 0
        for x in self.bins:
            i = 0
            while x.read(i):
                i += 1
                total += 1
        return total
            

    def get(self,key):
        ''' Returns the value for the given key, or None if value not found. '''
        location = hash(key) % self.numBins
        i = 0
        while self.bins[location].read(i):
            if self.bins[location].read(i)[0] == key:
                return self.bins[location].read(i)[1]
            i += 1
        return None

    def insert(self,key,value):
        ''' Adds <key,value> pair to the dictionary. '''
        location = hash(key) % self.numBins
        if (self.get(key) != None):
            i = 0
            while self.bins[location].read(i):
                if self.bins[location].read(i)[0] == key:
                    self.bins[location].deleteAtIndex(i)
                i += 1
        self.bins[location].append([key,value])
        return
        
    def keys(self):
        ''' Returns a python list of keys in the dictionary. '''
        keys= []
        for x in self.bins:
            i = 0
            while x.read(i):
                keys.append(x.read(i)[0])
                i += 1
        if keys == []:
            return None
        return keys
                
        
    def values(self):
        ''' Returns a python list of values in the dictionary. '''
        values= []
        for x in self.bins:
            i = 0
            while x.read(i):
                values.append(x.read(i)[1])
                i += 1
        if values == []:
            return None
        return values
        
    def remove(self,key):
        ''' Returns the <key,value> pair removed, or None if key not found. '''
        tup = [None,None]
        tup[0] = key
        tup[1] = self.get(key)
        location = hash(key) % self.numBins
        i = 0
        while self.bins[location].read(i):
            if self.bins[location].read(i)[0] == key:
                self.bins[location].deleteAtIndex(i)
            i += 1
        if tup == [None,None]:
            return None
        return tup
        
    def update(self,aDict):
        ''' Adds all <key,value> pairs from aDict to this MyDictionary. '''
        for x in aDict.items():
            self.insert(x[0],x[1])
        return
        
    def __str__(self):
        ''' Outputs dictionary's contents to a single formatted string. '''
        if len(self) == 0:
            return ''
        out = '['
        i = 0
        for x in self.items():
            out += str(x)
            i += 1
            if (i != len(self)):
                out += ', '
            else:
                out += ']'
        return out
            
        
    
        
    
