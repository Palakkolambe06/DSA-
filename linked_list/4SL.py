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

    # Find Middle and Delete Middle Node
    def findmid_del(self):
        if self.head == None:
            print("Linked List is empty")
            return

        slow = self.head
        fast = self.head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        print("Middle Node Deleted:", slow.data)

        if prev == None:
            self.head = self.head.next
        else:
            prev.next = slow.next


list1 = SLL()

n1 = Node(10)
n2 = Node(20)

list1.append(n1)
list1.append(n2)
list1.append(Node(30))
list1.append(Node(40))
list1.append(Node(50))

print("Original Linked List:")
list1.print()

list1.findmid_del()

print("Linked List After Deleting Middle Node:")
list1.print()