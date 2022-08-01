class BinaryTree:
    def __init__(self):
        self.root = Node(index=0)

    def append(self, data):
        if self.root.data == None:
            self.root.data = data
            return self.root.index

        current_node = self.root
        while True:
            if current_node.left == None:
                current_node.left = Node(index=current_node.index - 1, data=data)
                return current_node.left.index
            elif current_node.right == None:
                current_node.right = Node(index=current_node.index + 1, data=data)
                return current_node.right.index
            else:
                current_node = current_node.left

class Node:
    def __init__(self, index=None, data=None, left=None, right=None):
        self.index = index
        self.data = data
        self.left = left
        self.right = right

    def set_left(data):
        self.left = Node(index=self.index - 1, data=data)

    def set_right(data):
        self.right = Node(index=self.index + 1, data=data)
