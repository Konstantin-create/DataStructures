# Only for digits
class BinaryTree:
    def __init__(self):
        self.root = Node(index=0)

    def append(self, index: int):
        current_node = self.root
        while True:
            if current_node.index == index:
                raise TypeError(f'Your index is not unic')
            if index < current_node.index:
                if current_node.left is None:
                    current_node.left = Node(index=index)
                    return
                current_node = current_node.left
            elif index > current_node.index:
                if current_node.right is None:
                    current_node.right = Node(index=index)
                    return
                current_node = current_node.right

    def __repr__(self):
        return f'{self.root}'


class Node:
    def __init__(self, index=None, left=None, right=None):
        self.index = index
        self.left = left
        self.right = right

    def __repr__(self):
        return f'({self.index}, {self.left}, {self.right})'
