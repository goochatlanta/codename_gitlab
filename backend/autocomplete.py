class TrieNode(object):
    
    def __init__(self):
        self.children = {}
                


class Trie(object):
    
    def __init__(self):
        self.root = TrieNode()
        

    def search(self, word):
        
        currentNode = self.root
        
        for char in word:
            
            if currentNode.children.get(char):
                currentNode = currentNode.children[char]
            else:
                return None
        
        return currentNode
    
    
    def insert(self, word):
        
        currentNode = self.root
        
        for char in word:
            
            if currentNode.children.get(char):
                currentNode = currentNode.children[char]
            else:
                newNode = TrieNode()
                currentNode.children[char] = newNode
                
                currentNode = newNode
            
        currentNode.children["*"] = None
                      
            
            
            
    def collectAllWords(self, node=None, word="", words=[]):
        
        currentNode = node or self.root
        
        for key, childNode in currentNode.children.items():
            
            if key == "*":
                words.append(word)
            else:
                self.collectAllWords(childNode, word + key, words)
        
        return words
    
    
    def autocomplete(self, prefix):
        
        currentNode = self.search(prefix)
        
        if not currentNode:
            return None
        
        return self.collectAllWords(currentNode)
    

            
if __name__ == "__main__":
    
    index = 0
          
    try:     
        with open('codenames.txt', "r") as file:
            codeNames = file.read().splitlines()
    except Exception:
        print("codenames.txt does not exist")
    
    codeNameTrie = Trie()
    
    try:
        for element in codeNames:
            codeNameTrie.insert(element)
    
    except Exception:
        print("Error insertin CodeName word. ")


    while True:
        try:
            command = input("Enter 'Exit' to quit or\nEnter a letter or part of a CodeName word to see the autocomplete choices:   ")
            print()
            if command == "Exit":
                quit()
            else:
                try:
                    results = codeNameTrie.autocomplete(command.upper())               
                    
                    if results == None:
                        print('No CodeName words exist with that prefix. ')
                        print()

                    else:         
                        newWords = results[index:]
                        newLen = len(newWords)
                        print(newWords)
                        index += newLen 
                        print()
                    
                        
                except Exception:
                    print("Error autocompleting, try again. ")
        except Exception:
            print("Try again.")
    
