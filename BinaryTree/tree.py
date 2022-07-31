from pympler import asizeof


# Binary tree on tuple
class BinaryTree_on_tuples:
    __slots__ = ('tree')
    def __init__(self):
        self.tree = ()

    def append(self, key: int, data: any):
        if len(self.tree) == 0:
            self.tree = (key, data, None, None)
        else:
            pass # Append elements

    def _tmp_rec_check_index(self, tuple_to_check: tuple, index: int):
        if tuple_to_check[0] == index:
            return (tuple_to_check[0], tuple_to_check[1])
        if index > tuple_to_check[0]:
            return tuple_to_check[3]
        if index < tuple_to_check[0]:
            return tuple_to_check[2]

    def get_item(self, index: int): 
        tmp_tree = self.tree
        while True:
            responce = self._tmp_rec_check_index(tmp_tree, index)
            if not responce:
                raise IndexError(f'No such index {index}')
            elif len(responce) == 2:
                return responce[1]
            elif len(responce) == 4:
                tmp_tree = responce
 


tree = BinaryTree_on_tuples()
tree.tree = (12, 'root', (11, 'node1', (10, 'leave1', None, None), None), (15, 'node2', None, None))

print(tree.get_item(10))
print(asizeof.asizeof(tree))

