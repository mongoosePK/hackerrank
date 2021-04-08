# day24MoreLinkedLists.py
# william pulkownik
# remove linked list duplicates


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        previousNode = head
        currentNode = head.next
        
        # here we use a set to compare values with O(1) time
        values = set([previousNode.data])

        while currentNode:
            data = currentNode.data
            if data in values:
                # if the node's value is already present 
                # we point the previous node to the next node, unlinking the node from the list
                previousNode.next = currentNode.next
                currentNode = currentNode.next
            else:
                # the value is not in our set so we add it and 
                # advance the nodes
                values.add(currentNode.data)
                previousNode = currentNode
                currentNode = currentNode.next
        return head


mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 