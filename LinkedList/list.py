class LinkedList:
    __slots__ = ('head')
    def __init__(self, head_data=None):
        self.head = _Node(data=head_data)

    def insert_end(self, data=None) -> None:
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

    def insert(self, data=None) -> None:
        """Function to insert item to the head of linked list"""
        if self.head.data == None:
            self.head.data = _Node(data=data, next_item=self.head.next)
            return
        self.head = _Node(data=data, next_item=self.head)

    def pop_data(self, data) -> any:
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
        elif not current_node.next:
            previos_node.next = None
        else:
            previos_node.next = current_node.next
        return data

    def pop_end(self) -> any:
        """Function to delete element in the end of linked list"""
        current_node = self.head
        previos_node = current_node
        while True:
            if not current_node.next:
                break
            previos_node = current_node
            current_node = current_node.next
        
        data = current_node.data
        if current_node == previos_node:
            self.head = _Node()
            return data
        previos_node.next = None
        return data

    def pop(self) -> any:
        """Function to delete element in the head of linked list"""
        if self.head.next is None:
            data = self.head.data
            self.head = _Node()
            return data
        data = self.head.data
        self.head = self.head.next
        return data

    def find(self, data) -> object:
        """Function to find element by data. Return element and next items"""
        current_node = self.head
        while True:
            if current_node.data == data:
                return current_node
            if not current_node.next:
                return None
            current_node = current_node.next

    def isEmpty(self) -> bool:
        """Function to check is list empty"""
        return not self.head.next


    def reverse(self) -> None:
        current_list = self.__iter__()
        self.head = _Node()
        for item in current_list:
            self.insert(item)


    def __iadd__(self, other) -> object:
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

    def __len__(self) -> int:
        """Function to get lenght of linked list"""
        counter = 0
        if self.head.data is None:
            return counter
        if not self.head.next:
            return counter + 1

        current_node = self.head
        while True:
            counter += 1
            if not current_node.next:
                return counter
            current_node = current_node.next


    def __str__(self) -> str:
        """Function to return string from linked list"""
        output = []
        current_node = self.head
        while True:
            output.append(current_node.data)
            if not current_node.next:
                return str(output)
            current_node = current_node.next

    def __getitem__(self, key) -> object:
        """Magic method for self.find function"""
        return self.find(key)

    def __iter__(self) -> list:
        """Function to return list from linked list"""
        output = []
        current_node = self.head
        while True:
            output.append(current_node.data)
            if not current_node.next:
                return output
            current_node = current_node.next

    def __contains__(self, item) -> bool:
        """Function to check is item in linked list"""
        if self.head.data == item:
            return True
        current_node = self.head
        while True:
            if current_node.data == item:
                return True
            if not current_node.next:
                return False
            current_node = current_node.next

    def __reversed__(self):
        """Magic method for self.reversed function"""
        self.reverse()
    

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

