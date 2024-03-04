class Node:
    """A class representing a stack data structure."""
    def __init__(self, value):
        """
        Initializes a new Node with the given value.

        Parameters:
            value: The value to be stored in the node.
        """
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        """
        Initializes a new Stack with the given initial value.

        Parameters:
            value: The initial value to be added to the stack.
        """
        new_node = Node(value)
        self.top = new_node
        self.height = 1
        
    def print_stack(self):
        """
        Prints the values of all nodes in the stack, starting from the top.

        This method traverses the stack from the top to the bottom, printing the value of each node.
        """
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next
    
    def push(self, value):
        """
        Pushes a new value onto the top of the stack.

        Parameters:
            value: The value to be pushed onto the stack.
        """
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
    
    def pop(self):
        """
        Removes and returns the value from the top of the stack.

        Returns:
            The value removed from the top of the stack, or None if the stack is empty.
        """
        if self.height == 0:
            return None
        temp = self.top
        self.top = temp.next
        temp.next = None
        self.height -= 1
        return temp.value
    
    
# Create a Stack object named my_stack with an initial value of 1   
my_stack = Stack(1)

# Push values onto the stack
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)

# Print the values of all nodes in the stack, starting from the top

my_stack.print_stack()

print("--- POP ---")
# Remove and return the value from the top of the stack
print("Pop item -> ", my_stack.pop())

my_stack.print_stack()

print("--- POP ---")
print("Pop item -> ", my_stack.pop())
print("Push item -> ", my_stack.push(5))
my_stack.print_stack()
print("Pop item -> ", my_stack.pop())
print("Pop item -> ", my_stack.pop())
print("Pop item -> ", my_stack.pop())


my_stack.print_stack()
            