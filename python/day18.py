# day18.py
# wpulkownik
# 

import sys
class Node:
    def __init__(self, letter):
        self.letter = letter
        self.next = None
class Solution:
    '''
    implement the class with two methods, queue(str) and stack(str) 
    both methods will accept the same string but output them starting 
    FIFO(queue) and LIFO(stack)
    '''
    def __init__(self):
        self.stack_top = Node('bottom')
        self.qhead = None
        self.qtail = None

    def pushCharacter(self, letter):
        '''
        to push a string Node on top of the stack, we set the next() pointer to the 
        value immediately preceding it, then we set the stack top to point at the new node.
        '''
        stack_pointer = Node(letter)
        stack_pointer.next = self.stack_top.next
        self.stack_top.next = stack_pointer

    def enqueueCharacter(self, letter):
        '''
        to enqueue a Node, we set the initial queue node to the head and the tail.
        subsequent Nodes are linked from the tail and then set as the tail
        '''
        qptr = Node(letter)
        if self.qhead is None:
            self.qhead = self.qtail = qptr
        else: 
            self.qtail.next = qptr
            self.qtail = qptr

    def popCharacter(self):
        '''
        to pop a node, if we are not at the bottom of the stack, 
        we fill a temp variable with the pointer to the top of the stack
        then we point the top at the successive node
        '''
        if self.stack_top.next != 'bottom':
            pop = self.stack_top.next
            self.stack_top.next = self.stack_top.next.next
            return pop.letter
        
    def dequeueCharacter(self):
        '''
        to de-queue we make a temp variable for the head, then we point 
        the head at the next element in the queue
        '''
        head = self.qhead
        self.qhead = self.qhead.next
        return head.letter


# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    