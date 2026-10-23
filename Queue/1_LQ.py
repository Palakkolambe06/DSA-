# Linear queue using Lineked list
# Enqueue Operation 
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None 

class Queue:
     def __init__(self):
         self.front = self.rear = None

     def enqueue(self, new_node):
         if self.rear:
             self.rear.next = new_node
             self.rear = new_node
         else:
             self.front = self.rear = new_node
     def print(self):
         temp = self.front
         while temp:
             print(temp.data, end= "->")
             temp = temp.next

Q1 = Queue()
Q1.enqueue(Node(15))
Q1.enqueue(Node(20))
Q1.enqueue(Node(25))
Q1.enqueue(Node(30))
Q1.enqueue(Node(35))
Q1.print()




              
