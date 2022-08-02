class Stack:
    __slots__ = ('stack')
    def __init__(self, stack=[]):
        self.stack = list(stack)

    def push(self, item):
        """Function to add element to stack"""
        self.stack.append(item)

    def pop(self):
        """Function to get top element from stack and remove it"""
        if self.isEmpty():
            return None
        return self.stack.pop()
    
    def isEmpty(self):
        """Function to check is file empty"""
        return len(self.stack) == 0

    def top(self):
        """Function to get top element from stack without remove it"""
        if self.isEmpty():
            return None
        return self.stack[-1]

    def __iadd__(self, other):
        """Function to add element to Stack and save it in self.stack"""
        try:
            if type(other) == list:
                self.push(other)
                return self
            self.stack += other.stack
            return self
        except AttributeError:
            self.push(other)
            return self

    def __add__(self, other):
        """Function to add element to Stack"""
        try:
            if type(other) == list:
                return Stack(self.stack + other)
            return Stack(self.stack + other.stack)
        except AttributeError:
            return Stack(self.stack+ list(other))
    
    def __len__(self):
        """Function to get item lenght"""
        return len(self.stack)

    def __repr__(self):
        """Function to return item"""
        return f'Stack({self.stack})'
