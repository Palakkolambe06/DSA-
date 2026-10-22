
# Create a Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create a Stack class
class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    # Insert an element
    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    # Remove the top element
    def pop(self):
        if self.isempty():
            print("Stack is empty")
            return None

        temp = self.top
        self.top = self.top.next
        return temp.data

    # Display stack elements
    def print(self):
        temp = self.top
        print("Stack elements:")

        while temp:
            print(temp.data)
            temp = temp.next

    # Reverse the stack's linked list
    def reverse(self):
        prev = None
        temp = self.top

        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node

        self.top = prev


# Create a stack
st = Stack()

# Push elements
st.push(Node(10))
st.push(Node(100))
st.push(Node(45))
st.push(Node(70))
st.push(Node(80))

# Display original stack
st.print()

# Reverse the stack
st.reverse()

# Display reversed stack
print("After reversing:")
st.print()
