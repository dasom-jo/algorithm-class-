class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    def is_empty(self):
        if self.head is None:
            return True
        return False
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def pop(self):
        if self.is_empty():
            return None
        data = self.head.data
        self.head = self.head.next
        return data
    def peek(self):
        if self.is_empty():
            return None
        return self.head.data
    
my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
print(my_stack.pop())
print(my_stack.peek())