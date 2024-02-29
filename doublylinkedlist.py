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
    
    def prepend(self, value):
        """
        Adds a new node with the provided value to the beginning of the list.

        Parameters:
            value: Any - The value to be stored in the new node.

        Returns:
            bool: True if the node is successfully prepended, False otherwise.
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        """
        Removes and returns the value of the first node from the list.

        Returns:
            Any or None: The value of the removed node, or None if the list is empty.
        """
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp.value
        
    def get(self, index):
        """
        Retrieves the value of the node at the specified index in the list.

        Parameters:
            index: int - The index of the node to retrieve.

        Returns:
            Any or None: The value of the node at the specified index, or None if the index is out of range.
        """
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, index , -1):
                temp = temp.prev
        return temp
    
    def set_value(self, index, value):
        """
        Sets the value of the node at the specified index in the list.

        If the index is valid, the value of the node at that index is updated with the provided value.

        Parameters:
            index: int - The index of the node to set the value for.
            value: Any - The new value to assign to the node.

        Returns:
            bool: True if the value is successfully set, False otherwise (e.g., if the index is out of range).
        """
        temp =self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        """
        Inserts a new node with the provided value at the specified index in the list.

        Parameters:
            index: int - The index at which to insert the new node.
            value: Any - The value to be stored in the new node.

        Returns:
            bool: True if the node is successfully inserted, False otherwise (e.g., if the index is out of range).
        """
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        
        self.length += 1
        return True
        
    def remove(self, index):
        """
        Removes the node at the specified index from the list.

        Parameters:
            index: int - The index of the node to be removed.

        Returns:
            Any or None: The value of the removed node, or None if no removal is performed.
        """
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp.value    
    
            
my_doublylinked_list = DoublyLinkedList(1)
my_doublylinked_list.append(2)
my_doublylinked_list.append(3)
my_doublylinked_list.append(4)

my_doublylinked_list.print_list()
# print("---- after pop ----")
# my_doublylinked_list.pop()
# print("--- after prepend ---")
# my_doublylinked_list.prepend(1)

# print("--- pop first ----")
# print(my_doublylinked_list.pop_first())
# print(my_doublylinked_list.pop_first())
# print(my_doublylinked_list.pop_first())
# print(my_doublylinked_list.pop_first())

print("--- get ---")
print(my_doublylinked_list.get(3).value)

print("--- after set values ---")
my_doublylinked_list.set_value(2,7)
my_doublylinked_list.print_list()

print("--- after insert ---")
print(my_doublylinked_list.insert(2,3))
my_doublylinked_list.print_list()

print("--- after remove ---")
print(my_doublylinked_list.remove(3))
print("--- after remove ---")
my_doublylinked_list.print_list()
