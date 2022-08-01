class BinaryTree:
    def __init__(self):
        self.root = Node(index=0)

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
            

    def __repr__(self):
        return f'{self.root}'


class Node:
    def __init__(self, index=None, data=None, left=None, right=None):
        self.index = index
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return f'({self.index}, {self.data}, {self.left}, {self.right})'
