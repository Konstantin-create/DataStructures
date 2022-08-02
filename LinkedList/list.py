class LinkedList:
    __slots__ = ('head')
    def __init__(self, head_data=None):
        self.head = _Node(data=head_data)

    def insert(self, data=None):
        """Function to insert item to the end of linked list"""
        current_node = self.head
        while True:
            if current_node.next is None:
                current_node.next = _Node(data=data)
                return
            current_node = current_node.next

    def insert_head(self, data=None):
        """Function to insert item to the head of linked list"""
        self.head = _Node(data=data, next_item=self.head)

    def delete(self, data):
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
                return
            raise KeyError('You cant remove the last node!')
        if not current_node.next:
            previos_node.next = None
        else:
            previos_node.next = current_node.next

    def delete_end(self):
        """Function to delete element in the end of linked list"""
        current_node = self.head
        previos_node = current_node
        while True:
            if not current_node.next:
                break
            previos_node = current_node
            current_node = current_node.next

        if current_node == previos_node:
            raise KeyError('You cant remove the last node!')
        previos_node.next = None

    def delete_head(self):
        """Function to delete element in the head of linked list"""
        if not self.head.next:
            raise KeyError('You cant remove the last node!')
        self.head = self.head.next

    def find(self, data):
        current_node = self.head
        while True:
            if current_node.data = data:
                return current_node
            if not current_node.next:
                return None
            current_node = current_node.next


    def __repr__(self):
        """Function to print self"""
        return f'LinkedList({self.head})'

class _Node:
    __slots__ = ('data', 'next')
    def __init__(self, data=None, next_item=None):
        self.data = data
        self.next = next_item

    def __repr__(self):
        if self.next is None:
            return f'{self.data}'
        return f'{self.data}, {self.next}'

