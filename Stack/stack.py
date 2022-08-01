class Stack:
    __slots__ = ('stack')
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Function to add element to stack"""
        self.stack.append(item)

    def pop(self):
        """Function to get element from stack"""
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def __repr__(self):
        return f'Stack{self.stack}'
