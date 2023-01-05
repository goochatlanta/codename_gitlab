from scipy import spatial

def read_codename_words():
     ''' Converts .txt file with 400 codename words into a list.'''
     
     try:     
          with open('codenames.txt', "r") as file:
               out = file.readlines()
     except Exception:
          print("codenames.txt does not exist")

     return out     


def write_faster_file(fileName):
     ''' Attempted to speed up the process by pre-formatting the vectors, resulted
     in exact same output. Continue to search for faster alternatives. '''
     lines = read_vectors(fileName)
     
     try:     
          with open('vectors.txt', "w", encoding="utf-8") as file:
               for line in lines:
                    file.write(line)
     except Exception:
          print(fileName, "does not exist")            
     
     
def read_vectors(fileName):
     ''' Reads the .txt file with 6B tokens, 400K vocab, and 50 dimensions.
     Returns the list of lines. '''

     try:
          with open(fileName, 'r', encoding="utf-8") as file:
               lines = file.readlines()
     except Exception:
          print(fileName, "does not exist or is in the wrong format.")
          
     return lines


def create_dictionary(lines):
     ''' Creates a dictionary with 400K vocab words as keys and an array of dimensions
     as their values. '''
     
     vectorDict = {} 
     for line in lines:
          newLine = []
          values = line.split()
          word = values[0]
          vector = values[1:]
          for element in vector:
               newLine.append(float(element))
          vectorDict[word] = newLine
          
     return vectorDict
    

def distance(word, reference):
     ''' Performs cosine distance computation from scipy. CodeName word is found in the
     vector dictionary and the value (vectors) are used with each "closest word" provided. '''
     return spatial.distance.cosine(vectorDict[word], vectorDict[reference])
    

def closest_words(reference):
     ''' Uses the user-provided CodeName word and the vector dictionary to sort (i believe)
     all 400K words from closest to farthest.  Calls distance() to perform computation. '''
     return sorted(vectorDict.keys(), key=lambda word: distance(word, reference))

    
    
##### Main #####
#write_faster_file("glove.6B.50d.txt") 
codenames = read_codename_words()
vectors = read_vectors("glove.6B.50d.txt")
vectorDict = create_dictionary(vectors)

while True:
     try:
          command = input("Enter a CodeName to see the five closest words or enter Exit to quit:   ")
          print()
          if command == "Exit":
               quit()
          else:
               try:
                    print([(w, ", ".join(closest_words(w)[1:6])) for w in [command]])
                    print()
               except Exception:
                    print("Invalid CodeName word, try again. ")
     except Exception:
          print("Try again.")

