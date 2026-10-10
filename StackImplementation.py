class Stack:
    def __init__(self):
        # Initialize an empty list to store stack elements
        self.stack = []

    def push(self, item):
        """Add an element to the top of the stack."""
        self.stack.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        """Remove and return the top element of the stack. Raise error if empty."""
        if self.is_empty():
            return "Stack is empty! Cannot pop."
        return self.stack.pop()

    def peek(self):
        """View the top element of the stack without removing it."""
        if self.is_empty():
            return "Stack is empty! Nothing to peek."
        return self.stack[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Return the number of elements in the stack."""
        return len(self.stack)

    def display(self):
        """Display the current state of the stack."""
        return self.stack


# Example usage:
my_stack = Stack()

# 1. Push elements
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
print("Current Stack:", my_stack.display())

# 2. Peek at the top element
print("Top element (Peek):", my_stack.peek())

# 3. Pop elements
print("Popped element:", my_stack.pop())
print("Popped element:", my_stack.pop())

# 4. Check size and if empty
print("Stack size:", my_stack.size())
print("Is stack empty?", my_stack.is_empty())

# 5. Pop last element and try popping from empty stack
print("Popped element:", my_stack.pop())
print(my_stack.pop())
