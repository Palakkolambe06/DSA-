# dequeue function
# Linear queue using Lineked list
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

     def dequeue(self):
         if self.front:
             temp = self.front
             self.front = self.front.next
             if self.front == None:
                 self.rear = None
                 print("Now Queue is empty !!")
             temp = None
         else:
             print("Queue is empty")

     def print(self):
         temp = self.front
         while temp:
             print(temp.data, end= "->")
             temp = temp.next
         print()

Q1 = Queue()
Q1.enqueue(Node(15))
Q1.enqueue(Node(20))
Q1.enqueue(Node(25))
Q1.enqueue(Node(30))
Q1.enqueue(Node(35))
Q1.dequeue() 
Q1.print()
Q1.dequeue() 
Q1.dequeue() 
Q1.dequeue() 
Q1.print()
Q1.dequeue() 
Q1.enqueue(Node(40))
Q1.enqueue(Node(45))





              
