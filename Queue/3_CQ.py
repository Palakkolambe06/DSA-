# Circular Queue using Linked List

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class CQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, new_node):
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = self.rear = new_node

        self.rear.next = self.front

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return

        temp = self.front
        print("Deleted:", temp.data)

        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front

    def print(self):
        if self.front is None:
            print("Queue is empty")
            return

        temp = self.front

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.front:
                break

        print("(back to front)")


Q1 = CQueue()

Q1.enqueue(Node(15))
Q1.enqueue(Node(20))
Q1.enqueue(Node(25))
Q1.enqueue(Node(30))

Q1.dequeue()
Q1.print()

Q1.dequeue()
Q1.print()

Q1.dequeue()
Q1.print()

Q1.dequeue()
Q1.print()

Q1.dequeue()
Q1.print()

Q1.dequeue()
Q1.print()

Q1.enqueue(Node(40))
Q1.enqueue(Node(45))
Q1.print()