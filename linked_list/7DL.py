# Code 2 — Position insertion
# Use it when your practical asks you to insert a node at a specified position. This is the cleanest version for that task.
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # Insert at a specific position (1-based indexing)
    def insert_position(self, data, pos):
        new_node = Node(data)

        # Insert at the beginning
        if pos == 1:
            new_node.next = self.head

            if self.head is not None:
                self.head.prev = new_node

            self.head = new_node
            return

        p = 1
        temp = self.head

        while p != pos - 1 and temp is not None:
            temp = temp.next
            p += 1
        
        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next is not None:
            temp.next.prev = new_node

        temp.next = new_node

    # Display the list
    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")


# Main program
dll = DoublyLinkedList()

dll.insert_end(10)
dll.insert_end(20)
dll.insert_end(30)
dll.insert_end(40)

print("Original list:")
dll.display()

data = int(input("Enter data to insert: "))
pos = int(input("Enter position: "))

dll.insert_position(data, pos)

print("List after insertion:")
dll.display()