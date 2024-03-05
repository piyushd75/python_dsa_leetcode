class Node:
    """A class representing a queue data structure."""
    def __init__(self, value):
        """
        Initializes a new Node with the given value.

        Parameters:
            value: The value to be stored in the node.
        """
        self.value = value
        self.next = None

class Queue:
    """
    Queue class represents a linear data structure that follows the First In, First Out (FIFO) principle.
    
    Attributes:
        first (Node): A reference to the first node in the queue.
        last (Node): A reference to the last node in the queue.
        length (int): Represents the number of nodes in the queue.
    
    Methods:
        __init__(self, value): Initializes the Queue object with a new node containing the given value.
    """
    def __init__(self, value):
        """
        Initializes a new Queue object with a node containing the given value.
        
        Args:
            value: The value to be stored in the first node of the queue.
        """
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
        
    def print_queue(self):
        """
        Prints the values of all nodes in the queue starting from the first node.
        """
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next
    
    def enqueue(self, value):
        """
        Adds a new node with the given value to the end of the queue.

        Args:
            value: The value to be added to the queue.
        """
        new_node = Node(value)
        if self.first == None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
    
    def dequeue(self):
        """
        Removes and returns the value of the first node in the queue.

        If the queue is empty, returns None.

        Returns:
            The value of the first node in the queue.
        """
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp.value
            

my_queue = Queue(1)

my_queue.print_queue()

my_queue.enqueue(2)
my_queue.enqueue(3)

print("--- after enqueue ----")
my_queue.print_queue()

print("dequeue ->" ,my_queue.dequeue())
print("dequeue ->" ,my_queue.dequeue())
print("dequeue ->" ,my_queue.dequeue())

my_queue.print_queue()
