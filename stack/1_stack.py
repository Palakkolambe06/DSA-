# Create a Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create a Stack class
class Stack:
    def __init__(self):
        self.top = None

    # Check whether the stack is empty
    def isempty(self):
        return self.top is None

    # Insert an element into the stack
    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    # Remove the top element from the stack
    def pop(self):
        if self.isempty():
            print("Stack is empty")
            return None

        temp = self.top
        self.top = self.top.next
        return temp.data

    # Display all elements of the stack
    def print(self):
        temp = self.top

        print("Stack elements:")

        while temp:
            print(temp.data)
            temp = temp.next


# Create a stack object
st = Stack()

# Push elements into the stack
st.push(Node(10))
st.push(Node(100))
st.push(Node(45))
st.push(Node(70))
st.push(Node(80))

# Display the stack
st.print()

# Check whether the stack is empty
print("Is stack empty?", st.isempty())

# Remove the top element
print("Popped element:", st.pop())

# Display the stack after popping
st.print()