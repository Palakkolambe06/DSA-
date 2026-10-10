
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Create Linked List
    def create(self, values):
        for value in values:
            self.insert_end(value)

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    # 2. Traverse and print
    def traverse(self):
        current = self.head
        values = []

        while current:
            values.append(str(current.data))
            current = current.next

        print(" ".join(values))

    # 3. Insert at a specific position (0-based)
    def insert_at_position(self, data, position):
        if position < 0:
            return

        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head

        for _ in range(position - 1):
            if current is None:
                return
            current = current.next

        if current is None:
            return

        new_node.next = current.next
        current.next = new_node

    # 4. Find middle node
    def find_middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if slow:
            print(slow.data)
        else:
            print(-1)

    # 5. Delete node by value (first occurrence)
    def delete_node(self, value):
        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head

        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next

    # 6. Reverse linked list
    def reverse(self):
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    # 7. Sum consecutive pairs
    def consecutive_sums(self):
        current = self.head
        sums = []

        while current and current.next:
            sums.append(str(current.data + current.next.data))
            current = current.next

        print(" ".join(sums))


def solution():
    ll = LinkedList()

    # Enter the number of nodes
    n = int(input("Enter number of nodes: "))

    # Enter the node values separated by spaces
    values = list(map(int, input("Enter node values: ").split()))

    # Use only the first n values
    ll.create(values[:n])

    print("\nOriginal linked list:")
    ll.traverse()

    print("Middle node:")
    ll.find_middle()

    print("Consecutive pair sums:")
    ll.consecutive_sums()

    print("Reversed linked list:")
    ll.reverse()
    ll.traverse()


if __name__ == "__main__":
    solution()
