
# Create a Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create a Stack class
class Stack:
    def __init__(self):
        self.top = None

    # Check whether stack is empty
    def isempty(self):
        return self.top is None

    # 1. Push operation
    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node
        print("Element inserted")

    # 2. Pop operation
    def pop(self):
        if self.isempty():
            print("Stack is empty")
            return None

        temp = self.top
        self.top = self.top.next
        return temp.data

    # 3. Display stack
    def print(self):
        if self.isempty():
            print("Stack is empty")
            return

        temp = self.top

        print("Stack elements:")

        while temp:
            print(temp.data)
            temp = temp.next

    # 4. Reverse String using Stack
    def reverse_string(self):
        s = input("Enter a string: ")

        temp = Stack()

        for ch in s:
            temp.push(Node(ch))

        result = ""

        while not temp.isempty():
            result = result + temp.pop()

        print("Reversed String:", result)

    # 5. Reverse Stack using another Stack
    def reverse_stack(self):
        temp = Stack()

        while not self.isempty():
            temp.push(Node(self.pop()))

        self.top = temp.top

        print("Stack reversed successfully")


# Main Program
st = Stack()

while True:

    print("\n----- STACK MENU -----")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Reverse String")
    print("5. Reverse Stack")
    print("6. Exit")

    ch = input("Enter your choice: ").lower()

    if ch == "push":
        n = int(input("Enter element: "))
        st.push(Node(n))

    elif ch == "pop":
        print("Popped element:", st.pop())

    elif ch == "display":
        st.print()

    elif ch == "reverse string":
        st.reverse_string()

    elif ch == "reverse stack":
        st.reverse_stack()

    elif ch == "exit":
        print("Program ended")
        break

    else:
        print("Invalid choice")
