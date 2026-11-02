
# Create a Node class
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


# Create a Queue class
class Queue:
    def __init__(self):
        self.front = self.rear = None

    # 1. Enqueue operation
    def enqueue(self, new_node):
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = self.rear = new_node

        print("Element inserted")

    # 2. Dequeue operation
    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None

        temp = self.front
        value = temp.data

        self.front = self.front.next

        if self.front is None:
            self.rear = None

        print("Deleted element:", value)
        return value

    # 3. Display operation
    def print(self):
        if self.front is None:
            print("Queue is empty")
            return

        temp = self.front

        print("Queue elements:")

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # 4. Reverse Queue using Stack
    def reverse(self):
        stack = []
        temp = self.front

        while temp:
            stack.append(temp.data)
            temp = temp.next

        self.front = self.rear = None

        while len(stack) > 0:
            self.enqueue(Node(stack.pop()))

        print("Queue reversed")

    # 5. Merge two Queues
    def merge(self, q2):
        temp = q2.front

        while temp:
            self.enqueue(Node(temp.data))
            temp = temp.next

        print("Queues merged successfully")

    # 6. Check whether two Queues are Identical
    def identical(self, q2):
        temp1 = self.front
        temp2 = q2.front

        while temp1 and temp2:
            if temp1.data != temp2.data:
                print("Queues are not identical")
                return

            temp1 = temp1.next
            temp2 = temp2.next

        if temp1 is None and temp2 is None:
            print("Queues are identical")
        else:
            print("Queues are not identical")


# Main Program
Q1 = Queue()

while True:

    print("\n----- QUEUE MENU -----")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Reverse Queue")
    print("5. Merge Queues")
    print("6. Check Identical")
    print("7. Exit")

    ch = input("Enter your choice: ").lower()

    if ch == "enqueue":
        n = int(input("Enter element: "))
        Q1.enqueue(Node(n))

    elif ch == "dequeue":
        Q1.dequeue()

    elif ch == "display":
        Q1.print()

    elif ch == "reverse":
        Q1.reverse()

    elif ch == "merge":
        Q2 = Queue()

        n = int(input("How many elements in second queue? "))

        for i in range(n):
            value = int(input("Enter element: "))
            Q2.enqueue(Node(value))

        Q1.merge(Q2)

    elif ch == "identical":
        Q2 = Queue()

        n = int(input("How many elements in second queue? "))

        for i in range(n):
            value = int(input("Enter element: "))
            Q2.enqueue(Node(value))

        Q1.identical(Q2)

    elif ch == "exit":
        print("Program ended")
        break

    else:
        print("Invalid choice")
