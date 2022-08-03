class LinkedList:
    __slots__ = ('head')
    def __init__(self, head_data=None):
        self.head = _Node(data=head_data)

    def insert_end(self, data=None):
        """Function to insert item to the end of linked list"""
        if self.head.data == None:
            self.head.data = data
            return
        current_node = self.head
        while True:
            if current_node.next is None:
                current_node.next = _Node(data=data)
                return
            current_node = current_node.next

    def insert(self, data=None):
        """Function to insert item to the head of linked list"""
        if self.head.data == None:
            self.head.data = _Node(data=data, next_item=self.head.next)
            return
        self.head = _Node(data=data, next_item=self.head)

    def pop_data(self, data):
        """Function to delete element by data"""
        current_node = self.head
        previos_node = current_node
        while True:
            if current_node.data == data:
                break
            if not current_node.next:
                raise KeyError(f'No such element {data}')
            previos_node = current_node
            current_node = current_node.next
        
        if current_node == previos_node:
            if current_node.next:
                self.head = current_node.next
                return -1
            self.head = _Node()
        if not current_node.next:
            previos_node.next = None
        else:
            previos_node.next = current_node.next

    def pop_end(self):
        """Function to delete element in the end of linked list"""
        current_node = self.head
        previos_node = current_node
        while True:
            if not current_node.next:
                break
            previos_node = current_node
            current_node = current_node.next

        if current_node == previos_node:
            self.head = _Node()
        previos_node.next = None

    def pop(self):
        """Function to delete element in the head of linked list"""
        if self.head.next is None:
            self.head = _Node()
            return
        self.head = self.head.next

    def find(self, data):
        """Function to find element by data. Return element and next items"""
        current_node = self.head
        while True:
            if current_node.data == data:
                return current_node
            if not current_node.next:
                return None
            current_node = current_node.next

    def isEmpty(self):
        """Function to check is list empty"""
        return not self.head.next


    def __iadd__(self, other):
        """Function to add element to queue and asign a value to queue. Return self"""
        try:
            current_other_node = other.head
            while True:
                self.insert(current_other_node.data)
                if not current_other_node.next:
                    return self
                current_other_node = current_other_node.next
        except AttributeError:
            if type(other) is list:
                for element in other:
                    self.insert(element)
                return self
            self.insert(other)
            return self

    def __repr__(self):
        """Function to print self"""
        output = []
        current_node = self.head
        while True:
            output.append(current_node.data)
            if current_node.next == None:
                break
            current_node = current_node.next
        return f'LinkedList({output})'

class _Node:
    __slots__ = ('data', 'next')
    def __init__(self, data=None, next_item=None):
        self.data = data
        self.next = next_item

    def __repr__(self):
        if self.next is None:
            return f'{self.data}'
        return f'{self.data}, {self.next}'

