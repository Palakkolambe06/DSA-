class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, new_node, pos):
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        p = 1
        temp = self.head

        while p != pos - 1 and temp is not None:
            temp = temp.next
            p += 1

        if temp is None:
            raise IndexError("Position out of range")

        new_node.next = temp.next
        temp.next = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

list1 = LinkedList()

list1.insert(Node(10), 1)
list1.insert(Node(20), 2)
list1.insert(Node(30), 3)
list1.insert(Node(25), 3)

print("Linked List:")
list1.print_list()