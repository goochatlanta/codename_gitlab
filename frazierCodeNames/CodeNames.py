
from scipy import spatial
import PySimpleGUI as sg 
import autocomplete


def read_codename_words(fileName):
     ''' Converts .txt file with 400 codename words into a list.'''
     
     results = []
     try:     
          with open(fileName, "r") as file:
               results = file.readlines()
          for index in range(0, len(results)):
               results[index] = results[index].strip()              
     except Exception:
          print(fileName, "does not exist")            
     
     return results
     
     
def read_vectors(fileName):
     ''' Reads the .txt file with 25K vocab words and 50 dimensions.
     Returns the list of lines. '''

     try:
          with open(fileName, 'r', encoding="utf-8") as file:
               lines = file.readlines()
     except Exception:
          print(fileName, "does not exist") 
          
     return lines


def create_dictionary(lines):
     ''' Creates a Python dictionary with 25K vocab words as keys and an array of dimensions
     as their values. Returns the filled dictionary.'''
     
     vectorDict = {} 
     for line in lines:
          newLine = []
          values = line.split()
          word = values[0]                          # First list element is the vocab word
          vector = values[1:]                       # The rest of the list elements are the vector floats
          for element in vector:
               newLine.append(float(element))       # Ensure the element is a float
          vectorDict[word] = newLine                # Insert each Key, Value pair
          
     return vectorDict

# Reference: https://jsomers.net/glove-codenames/
def distance(word, reference):
     ''' Performs cosine distance computation from scipy. CodeName word is found in the
     vector dictionary and the value (vectors) are used with each "closest word" provided. '''
     return spatial.distance.cosine(vectorDict[word], vectorDict[reference])
 
    
# Reference: https://jsomers.net/glove-codenames/
def closest_words(reference):
     ''' Uses the user-provided CodeName word and the vector dictionary to sort (i believe)
     all 400K words from closest to farthest.  Calls distance() to perform computation. '''
     return sorted(vectorDict.keys(), key=lambda word: distance(word, reference))


# Reference: https://jsomers.net/glove-codenames/
def goodness(word, answers, bad):
     ''' For a given clue (of the 25K), returns the difference between the sum of distances from 
     the bad word and the sum of the distances for good words. '''
     if word in answers + bad: return -999
     return sum([distance(word, b) for b in bad]) - 4.0 * sum([distance(word, a) for a in answers])


# Reference: https://jsomers.net/glove-codenames/
def minimax(word, answers, bad):
     ''' For a given clue (of the 25K), returns the difference between the minimum distance from 
     the bad word and the maximum distances for good words. '''     
     if word in answers + bad: return -999
     return min([distance(word, b) for b in bad]) - max([distance(word, a) for a in answers])


# Reference: https://jsomers.net/glove-codenames/
def candidates(answers, bad, size=5):
     ''' Determines goodness and minimax of all 25K words for given good words and bad words. 
     Sorts the top 250 words, formats them and returns a list of the best clues. '''
     best = sorted(vectorDict.keys(), key=lambda w: -1 * goodness(w, answers, bad))
     res = [(str(i + 1), "{0:.2f}".format(minimax(w, answers, bad)), w) for i, w in enumerate(sorted(best[:250], key=lambda w: -1 * minimax(w, answers, bad))[:size])]
     return [(". ".join([c[0], c[2]]) + " (" + c[1] + ")") for c in res]

    
    

##########################################################
#testing-related

# Create a list of codename words by reading the .txt
codenames = read_codename_words('codenames.txt')

# Create a list of words and dimensions from the .txt
vectors = read_vectors('glove.25k.50d.txt')

# Create a python dictionary with the 400K words (key = word, value = list of dimensions)
vectorDict = create_dictionary(vectors)

# Create the autocomplete Trie 
auto = autocomplete.Trie()
for element in codenames:
     auto.insert(element)  
     
good = ['africa', 'agent', 'air']
bad = ['box']
print(candidates(good,bad))


          
 