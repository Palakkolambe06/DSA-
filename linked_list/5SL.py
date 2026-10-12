# Singly Linear Linked List

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    # Delete First Node
    def delete_first(self):
        if self.head == None:
            print("Linked List is empty")
        else:
            self.head = self.head.next

    # Delete Last Node
    def delete_last(self):
        if self.head == None:
            print("Linked List is empty")
        elif self.head.next == None:
            self.head = None
        else:
            temp = self.head

            while temp.next.next:
                temp = temp.next

            temp.next = None


list1 = SLL()

list1.append(Node(10))
list1.append(Node(20))
list1.append(Node(30))
list1.append(Node(40))
list1.append(Node(50))

print("Original Linked List:")
list1.print()

list1.delete_first()
print("After Deleting First Node:")
list1.print()

list1.delete_last()
print("After Deleting Last Node:")
list1.print()