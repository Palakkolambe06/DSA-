# Code 1 — Traversal
# Use it when practising basic doubly linked list creation and forward/backward traversal.
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # Display forward
    def display_forward(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    # Display backward
    def display_backward(self):
        temp = self.head

        if temp is None:
            print("List is empty")
            return

        while temp.next is not None:
            temp = temp.next

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")


# Main program
dll = DoublyLinkedList()

dll.insert(10)
dll.insert(20)
dll.insert(30)
dll.insert(40)

print("Forward traversal:")
dll.display_forward()

print("Backward traversal:")
dll.display_backward()