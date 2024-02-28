class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Linkedlist:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
            
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
        
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=  1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp.value
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next =temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        pre = self.get(index-1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True  
    
        
my_linked_list = Linkedlist(1)

my_linked_list.append(4)
# my_linked_list.append(7)
# my_linked_list.append(9)
# my_linked_list.append(11)
# my_linked_list.append(3)
# print("--- linked list before pop ---")
my_linked_list.print_list()

# print("--- linked list pop value ---")
# print(my_linked_list.pop())
# print(my_linked_list.pop())

# print("--- linked list after pop ---")
# my_linked_list.print_list()

# print("--- now prepend value ---")
# my_linked_list.prepend(8)
# my_linked_list.prepend(7)
# my_linked_list.print_list()

# print("--- now pop first value ---")
# print(my_linked_list.pop_first())
# print(my_linked_list.pop_first())
# print(my_linked_list.pop_first())
# print("--- linked list after pop_first ---")
# my_linked_list.print_list()

# print("--- get value by index ---")
# print(my_linked_list.get(3))
# print(my_linked_list.set_value(0, 9))
print("--- after set value by index ---")
my_linked_list.print_list()

my_linked_list.insert(1, 2)
my_linked_list.insert(2, 3)
print("--- after insert value ---")
my_linked_list.print_list()

# my_linked_list.remove(2)
# print("--- after remove value ---")
# my_linked_list.print_list()

my_linked_list.reverse()
print("--- after reverse value ---")
my_linked_list.print_list()
