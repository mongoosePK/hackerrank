# day15.py
# wpulkownik
# linked lists

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data): 
        n= Node(data)
        if head is None:
            return n
        elif head.next is None:
            head.next = n
        else:
            self.insert(head.next, data)
        return head
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  