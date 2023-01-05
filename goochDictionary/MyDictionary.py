
import copy
import LinkedList # LL has been changed to include LL.getCount()
import pdb

def checkNumeric(value):
    if not isinstance(value, int) and not isinstance(value, float):
        raise RuntimeError(str(value) + ' is not a number')
    return value


def checkPositive(value):
    value = checkNumeric(value)
    if value <= 0:
        raise RuntimeError(str(value) + ' is not a positive value')
    return value

########################################################
#constructor

class MyDictionary(object):
    '''Custom Dictionary Class
    
    Description of myDictionary custom class.
    Attributes: 
    __bins__ is a list of cells that keys are hashed to
    __numBins__ is the length of the list of cells
    
    Rules: 
    attributes of myDict are immutable
    there are a positive number of bins
    *contains keys in set property w.r.t keys
    
    Special feature: this MyDictionary class relies on an altered version of LinkedList.
    LinkedList has a new function called GetCount that counts how long the LinkedList is.
    '''

    def __init__(self, size):
        '''Inits custom dictionary called MyDictionary with a list of bins and the length of that list of bins.'''

        #Rules of Sevens for numBins
        #I never want zero bins, so for the positive numeric numbers, I set bins to 10  
        if 0 < size <= 7 and checkNumeric(size):
            self.__numBins =  10
            
        #For any other value given, I check positive and set Rule of 7s    
        else:
            self.__numBins = checkPositive( ((size // 7) + 1) * 10 ) #figure out the pattern


        self.__bins = [None] * checkPositive(self.__numBins) 





    @property
    def numBins(self):
            return self.__numBins

    @property
    def bins(self):
            return self.__bins

 
 #Check unassignability
    @bins.setter
    def bins(self, value):
        print("Error: attribute can't be modified.")


    @numBins.setter    
    def numBins(self, value):
        print("Error: attribute can't be modified.")

########################################################
#public methods a.k.a. Behaviors of custom class myDictionary



    def __len__(self): 
        ''' Returns how many pairs are in the dictionary'''
        return len(self.items())






    def insert(self, key, value):
        '''Add a new key value pair to the dictionary'''
        
        hashedKey = hash(key)

        indexBin = (hashedKey % self.__numBins  ) #if there are 20 bins - will it ever pick zero? Will it sometimes pick 20?
        
        if self.__bins[indexBin] == None:
            self.__bins[indexBin] = LinkedList.LinkedList() #an assignment, any variable can be anything

        else: 
            for indexLL in range( 0, self.__bins[indexBin].getCount() ):
                pair = self.__bins[indexBin].read(indexLL)
               
                if key == pair[0]:
                    self.__bins[indexBin].deleteAtIndex(indexLL)
                    break #because found the duplicate

        self.__bins[indexBin].append((key, value)) 






    def items(self):   
        '''Returns a Python list of <key,value> pairs'''
        
        itemsList = []

        for indexBin in range( 0, self.__numBins ): 

            if self.__bins[indexBin] == None:
                continue
                

            lengthLL = self.__bins[indexBin].getCount()

            for indexLL in range( 0, lengthLL ):
                
                pair = self.__bins[indexBin].read(indexLL) 

                itemsList.append(pair)  

        return itemsList                    





    def get(self, key): # scan linkedList within bin
        '''Returns the value, or None if not found'''

        #create list of items using items() function
        itemsList = self.items()

        for item in itemsList:

            if key == item[0]:
                return item[1]

        return None






    def keys(self):
        '''list of keys in custom dictionary'''
        keysList = []

        #create list of items using items() function
        itemsList = self.items()

        for item in itemsList:
            getKey = item[0]

            keysList.append(getKey)

        return keysList






    def values(self):
        '''list of values in custom dictionary'''
        valuesList = []

        #create list of items using items() function
        itemsList = self.items()

        for item in itemsList:
            getValue = item[1]

            valuesList.append(getValue)

        return valuesList





    def remove(self, key): 
        '''returns key/val pair removed or None if not found'''
        hashedKey = hash(key)

        indexBin = (hashedKey % self.__numBins  ) #if there are 20 bins - will it ever pick zero? Will it sometimes pick 20?
        
        if self.__bins[indexBin] == None:
            return None

        else: 
            for indexLL in range( 0, self.__bins[indexBin].getCount() ):
                pair = self.__bins[indexBin].read(indexLL)
               
                if key == pair[0]:
                    self.__bins[indexBin].deleteAtIndex(indexLL)
                    
                    return pair

        return None
 






    def update(self, aDict): 
        '''adds all key/value pairs from into this custom dictionary'''

        #getting list of tuples frm aDict
        aDictList = aDict.items()

        for item in aDictList:
            #insert hashes keys of aDict and deletes conflicting key-values based on key equivalence
            self.insert(item[0], item[1])






# ########################################################
# #private methods
# deep and shallow copy are available through the imported module copy (at top)

    def __str__(self):
        
        allitems = self.items()
        output = " "

        for pair in allitems:
            output += str(pair) + " " # seperated by a space
        return output

   # __ne__ is not necessary to implement for Python 3 as this is the default behavior.

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return  NotImplemented


    def __hash__(self):
        return hash(tuple( sorted(self.__dict__.items() ) ) )
#################################################################
#testing related

def test():
    print('start')

    #breakpoint()
    d = MyDictionary(1)
   
    print( 'len(d):', len(d) ) #tested for simple list of bins.
    d.insert('c' , 1)
    print( 'len(d):', len(d) ) #tested for simple list of bins.

    d.insert('d' , 46)
    print( 'len(d):', len(d) )

    d.insert('e' , 4)
    print( 'len(d):', len(d) )

    #breakpoint()
    print(d.items())

    print( 'keys:', d.keys() )
    print( 'values:', d.values() )

    d.remove( 'c' )
    print( 'removed(d):', d.items())
    print( 'len(d):', len(d) )

    e = dict()
    e[1] = 'c'
    e[2] = 'd'
    d.update(e)
    print( 'len(d):', len(d) )
    print( 'keys:', d.keys() )
    print( 'values:', d.values() )
    print( 'items:', d.items() )

    print(d.get(1))
    print(d.get(None))
    print(d.get(99))
    

    try:
        d.numBins = 5
    except Exception as e:
        print('checking numBins unassignability, exception caught: ', e) #46:00 Loren asks, "can I change the bins attribute? List attribute? How can I manage that?"
        
    try:
        d.bins = 5 
    except Exception as e:
        print('checking binsList unassignability, exception caught: ', e)
     
#################################################################
#main
 
if __name__=="__main__":
    test()



