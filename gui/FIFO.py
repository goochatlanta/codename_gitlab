#FIFO Queue
#
# CS3021 LL Project
#
# winter 2019
# last updated: 04 Jan 2019
#

## https://www.koderdojo.com/blog/coding-a-queue-abstract-data-type-using-a-linked-list-in-python

import LinkedList

class FIFO(object):
    ''' Implement, you will need to call appropriate LinkedList functionality.
        FIFO has-a Linked List.
        Generate appropriate docstrings.
        Do not write code to duplicate any LL behaviors in this file
        Do not change LinkedList. ''' 

    def __init__(self):
        """Initialize the use of LinkedList inside stack."""
        self.__QLL = LinkedList.LinkedList()
        self.tail = 0

    def add(self, dataItem):
        """Insert the given item at the head of this stack.
        Running time: O(1) - just does insert, which is O(1)"""
        self.__QLL.insertAtIndex(0,dataItem)
        self.tail += 1

    def remove(self):
        """Remove and return the item at the tail of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) - since tail, it happens easily."""
        if self.__QLL.empty():
            return None
        else: # here list is not empty
            answer = self.__QLL.read(self.tail-1) # list[len-1]
            self.__QLL.deleteAtIndex(self.tail-1)
            self.tail -= 1
            return answer

    def empty(self):
        """Return True if this stack is empty, or False otherwise."""
        return self.__QLL.empty()

    
    def __str__(self):
        """Return a string representation of this stack."""
        return self.__QLL.__str__()


##########################################################
#testing-related

##def fifotest():
##    q = FIFO()
##    q.remove()
##    print(q)
##    print('remove last item', q.remove())
##    q.add(4)
##    print(q)
##    print('remove last item', q.remove())
##########################################################
#main


if __name__=="__main__":
##    fifotest()
    q = FIFO()
    print('this is our queue:', q)  

