class Node:
    def __init__(self, value):
        """
        Initializes a node for a doubly linked list.

        Parameters:
            value: Any - The value to be stored in the node.

        Attributes:
            value: Any - The value stored in the node.
            next: Node or None - Reference to the next node in the list. Default is None.
            prev: Node or None - Reference to the previous node in the list. Default is None.
        """
        self.value = value
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    """
    Implementation of a doubly linked list.

    Attributes:
        head: Node or None - Reference to the first node in the list.
        tail: Node or None - Reference to the last node in the list.
        length: int - Number of nodes in the list.
    """
    def __init__(self,value):
        """
        Initializes a doubly linked list with a single node containing the provided value.

        Parameters:
            value: Any - The value to be stored in the initial node.
        """
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """
        Prints the values of all nodes in the list.
        """
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
            
    def append(self,value):
        """
        Appends a new node with the provided value to the end of the list.

        Parameters:
            value: Any - The value to be stored in the new node.

        Returns:
            bool: True if the node is successfully appended, False otherwise.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
            
    def pop(self):
        """
        Removes and returns the last node from the list.

        Returns:
            Node or None: The removed node, or None if the list is empty.
        """
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
            
my_doublylinked_list = DoublyLinkedList(1)
my_doublylinked_list.append(2)
my_doublylinked_list.append(3)
my_doublylinked_list.append(4)

my_doublylinked_list.print_list()
print("---- after pop ----")
my_doublylinked_list.pop()
my_doublylinked_list.print_list()