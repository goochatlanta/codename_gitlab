# autocomplete.py
#
# Reference: A Common Sense Guide to Data Structures and Algorithms Second Edition
# Class design and functions were used from the reference with minor adjustments to
# behaviors and function returns.


class TrieNode(object):
    ''' Trie is a collection of nodes that point to other nodes. '''
    
    def __init__(self):
        self.children = {}
                


class Trie(object):
    ''' Tracks the root node, begins with an empty TrieNode. '''
    
    def __init__(self):
        self.root = TrieNode()
        

    def search(self, word):
        ''' Establishes the current node, iterates over the word being searched,
        and finds children with the character key. If no children have the key,
        returns None. If it does, continue down by shifting the current node. '''
        currentNode = self.root
        
        for char in word:
            
            if currentNode.children.get(char):
                currentNode = currentNode.children[char]
            else:
                return None
        
        return currentNode
    
    
    def insert(self, word):
        '''  Establishes the current node, iterates over the word being inserted,
        determine if children alread have that key.  If so, update current node's
        children.  If not, create the new child. Asterisks indicate end of a word. '''
        currentNode = self.root
        
        for char in word:
            
            if currentNode.children.get(char):
                currentNode = currentNode.children[char]
            else:
                newNode = TrieNode()
                currentNode.children[char] = newNode
                
                currentNode = newNode
            
        currentNode.children["*"] = None
                      
            
    def collectAllWords(self, node=None, word='', words=[]):
        ''' Recursively returns an array of all words in the Trie startind at a 
        particular node. The starting node is the prefix entered in autocomplete. '''
        
        currentNode = node or self.root
        
        for key, childNode in currentNode.children.items():
            
            if key == "*":
                words.append(word)
            else:
                self.collectAllWords(childNode, word + key, words)
        
        return words
    
    
    def autocomplete(self, prefix):
        ''' Returns the completed words based on an input prefix. 
        Modified to include the prefix in the final words.'''
        
        currentNode = self.search(prefix)
        
        if not currentNode:
            return None
        
        endWords = self.collectAllWords(currentNode)
        
        for i in range(0,len(endWords)):
            endWords[i] = prefix + endWords[i]
        
        return endWords 
    


#  end class  
#####################################################


