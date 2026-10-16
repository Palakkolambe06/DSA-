# Code 3 — Multiple operations
# Use it to learn how creation, insertion, and deletion fit together, but fix the pointer bugs before relying on it.

class Node:
    def __init__(self,value):
        self.prev=None
        self.data=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def create(self,new_node):
        if self.head==None: #will be executed once for first node
            self.head=new_node
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp
        

    def insert(self,new_node,pos):
        if pos==1:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node

        else:
            p=1
            temp=self.head
            while(p!=pos-1 and temp.next): #temp.next is used to append at last position if invalid position is given
                temp=temp.next
                p+=1
            if temp.next: #for last position
                temp.next.prev=new_node
            new_node.prev=temp
            new_node.next=temp.next
            temp.next=new_node


    def delete(self,value):
        temp=self.head
        prev=None
        if temp.data==value:
            self.head=temp.next
        else:
            while(temp.data!=value and temp):
                prev=temp
                temp=temp.next
                if temp==None:
                    print("value not present")
                    return
            prev.next=temp.next
            temp=None




    def print(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
    
    

list1=LinkedList()
n1=Node(10)
n2=Node(20)
list1.create(n1)
list1.create(n2)
list1.create(Node(30))
list1.insert(Node(53),20)
list1.print()

# list1.delete(65)
# list1.print()