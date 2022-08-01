class BinaryTree:
    __slots__ = ('root')
    def __init__(self, index=0, data=None):
        self.root = Node(index=index, data=data)

    def append(self, index: int, data: any):
        """Function to append digit to tree"""
        current_node = self.root
        while True:
            if current_node.index == index:
                raise TypeError(f'Your index is not unic')
            if index < current_node.index:
                if current_node.left is None:
                    current_node.left = Node(index=index, data=data)
                    return
                current_node = current_node.left
            elif index > current_node.index:
                if current_node.right is None:
                    current_node.right = Node(index=index, data=data)
                    return
                current_node = current_node.right

    def find(self, index):
        """Function to find Node by index"""
        current_node = self.root
        while True:
            if current_node is None:
                raise IndexError(f'No such index {index}')
            if current_node.index == index:
                return current_node
            elif index < current_node.index:
                current_node = current_node.left
            elif index > current_node.index:
                current_node = current_node.right

    def get_depth(self):
        """function to find the depth of a tree"""
        layer = 0
        current_node = self.root
        while True:
            if current_node.left == None:
                break
            layer += 1
            current_node = current_node.left
        return layer

    def del_item(self, index):
        current_node = self.root
        previous_node = current_node
        while True:
            if current_node.index == index:
                if current_node.left is None and current_node.right is None:
                    if previous_node.left == current_node:
                        previous_node.left = None
                    else:
                        previous_node.right = None
                    return
                else:
                    raise KeyError('You can delete only leaves, not nodes')
            else:
                previous_node = current_node
                if index < current_node.index:
                    current_node = current_node.left
                elif index > current_node.index:
                    current_node = current_node.right
                else:
                    raise KeyError(f'No such index {index}')
            
    def __setitem__(self, key, value):
        if type(key) is int:
            self.append(key, value)
            return
        raise KeyError('Key have to be int')

    def __getitem__(self, key):
        if type(key) is int:
            return self.find(key)
        raise KeyError('Key have to be int')

    def __repr__(self):
        return f'{self.root}'


class Node:
    __slots__ = ('index', 'data', 'left', 'right')
    def __init__(self, index=None, data=None, left=None, right=None):
        self.index = index
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return f'({self.index}, {self.data}, {self.left}, {self.right})'
