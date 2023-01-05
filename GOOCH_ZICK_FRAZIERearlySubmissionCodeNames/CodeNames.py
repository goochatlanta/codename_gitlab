
from scipy import spatial
import PySimpleGUI as sg 
import autocomplete
import MyDictionary
import FIFO

class CodeNames(object):
     ''' Attributes are a MyDictionary of 400 CodeName words, a python dict of
     25l words and vectors. '''
     
     
     def __init__(self):
          
          self.__names = MyDictionary.MyDictionary(400)
          
          self.__vectors = {}
          
          self.__queue = FIFO.FIFO()
     
          self.__hash = None
     
     @property
     def names(self):
          ''' Ensures our names cannot be modified by the user.'''
          return self.__names 
     
     
     @property
     def vectors(self):
          ''' Ensures our vectors cannot be modified by the user.'''
          return self.__vectors       
     
     
     @property
     def queue(self):
          ''' Ensures our FIFO queue cannot be modified by the user.'''
          return self.__queue              



     def read_codename_words(self):
          ''' Converts .txt file with 400 codename words into a MyDictionary object.'''
          
          results = []
          try:     
               with open("codenames.txt", "r") as file:
                    results = file.readlines()
               for index in range(0, len(results)):
                    results[index] = results[index].strip()              
          except Exception:
               print("codenames.txt does not exist")            
          
          for word in results:
               self.__names.insert(word, 0)
          
          
     def read_vectors(self):
          ''' Reads the .txt file with 25K vocab words and 50 dimensions.
          Returns the list of lines. '''
     
          try:
               with open("glove.25k.50d.txt", 'r', encoding="utf-8") as file:
                    lines = file.readlines()
          except Exception:
               print("glove.25k.50d.txt does not exist") 
               
          return lines
     
     
     def create_dictionary(self):
          ''' Creates a Python dictionary with 25K vocab words as keys and an array of dimensions
          as their values. Returns the filled dictionary.'''
          
          lines = self.read_vectors()
          
          for line in lines:
               newLine = []
               values = line.split()
               word = values[0]                          # First list element is the vocab word
               vector = values[1:]                       # The rest of the list elements are the vector floats
               for element in vector:
                    newLine.append(float(element))       # Ensure the element is a float
               self.__vectors[word] = newLine            # Insert each Key, Value pair
               
     
     # Reference: https://jsomers.net/glove-codenames/
     def distance(self, word, reference):
          ''' Performs cosine distance computation from scipy. CodeName word is found in the
          vector dictionary and the value (vectors) are used with each "closest word" provided. '''
          return spatial.distance.cosine(self.vectors[word], self.vectors[reference])
      
         
     # Reference: https://jsomers.net/glove-codenames/
     def closest_words(self, reference):
          ''' Uses the user-provided CodeName word and the vector dictionary to sort (i believe)
          all 400K words from closest to farthest.  Calls distance() to perform computation. '''
          return sorted(self.vectors.keys(), key=lambda word: self.distance(word, reference))
     
     
     # Reference: https://jsomers.net/glove-codenames/
     def goodness(self, word, answers, bad):
          ''' For a given clue (of the 25K), returns the difference between the sum of distances from 
          the bad word and the sum of the distances for good words. '''
          if word in answers + bad: return -999
          return sum([self.distance(word, b) for b in bad]) - 4.0 * sum([self.distance(word, a) for a in answers])
     
     
     # Reference: https://jsomers.net/glove-codenames/
     def minimax(self, word, answers, bad):
          ''' For a given clue (of the 25K), returns the difference between the minimum distance from 
          the bad word and the maximum distances for good words. '''     
          if word in answers + bad: return -999
          return min([self.distance(word, b) for b in bad]) - max([self.distance(word, a) for a in answers])
     
     
     # Reference: https://jsomers.net/glove-codenames/
     def candidates(self, answers, bad, size=5):
          ''' Determines goodness and minimax of all 25K words for given good words and bad words. 
          Sorts the top 250 words, formats them and returns a list of the best clues. '''
          for i in range(0, len(answers)):
               answers[i] = answers[i].lower()
          
          for j in range(0, len(bad)):
               bad[j] = bad[j].lower()
          
          best = sorted(self.__vectors.keys(), key=lambda w: -1 * self.goodness(w, answers, bad))
          res = [(str(i + 1), "{0:.2f}".format(self.minimax(w, answers, bad)), w) for i, w in enumerate(sorted(best[:250], key=lambda w: -1 * self.minimax(w, answers, bad))[:size])]
          
          candidates = [(". ".join([c[0], c[2]]) + " (" + c[1] + ")") for c in res]
          for x in candidates:
               self.queue.add(x)

    
     def validateInput(self, value):
          '''Takes user inputs and verifies that they are in the 400 words dictionary '''
          
          if not isinstance(value, str):
               raise TypeError(str(value) + ' is not a string.')          
          
          elif self.names.get(value.upper()) == None:
               return False
          
          return True     
    
    
     def next_clue(self):
          '''Returns the next item in the queue '''
          return self.__queue.remove()
            
   
        
##########################################################
# private function

def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return  NotImplemented  

# We are not incorporating copy, deepcopy, hash in in the __int__

##########################################################
##testing-related

## Create a list of codename words by reading the .txt
#codenames = read_codename_words('codenames.txt')

## Create a list of words and dimensions from the .txt
#vectors = read_vectors('glove.25k.50d.txt')

## Create a python dictionary with the 400K words (key = word, value = list of dimensions)
#vectorDict = create_dictionary(vectors)

     
#good = ['africa', 'agent', 'air']
#bad = ['box']
#print(candidates(good,bad))


          
 