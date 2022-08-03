class DirectedGraph:
    __slots__ = ('head')
    def __init__(self, data=None):
        self.head = Vertex(0, data=data)
    
    def insert(self, data=None, outgoing=None, ingoing=None) -> None:
        """Function to insert a new vertex to graph"""
        if not self.head:
            if self.head.data is None:
                self.head = Vertex(index=0, data=data, x=outgoing, y=ingoing)
                return
            self.head.x = Vertex(index=1, data=data, x=outgoing, y=ingoing)
            return

        index = 0
        current_vertex = self.head
        while True:
            if not current_vertex.x:
                current_vertex.x = Vertex(index=index, data=data, x=outgoing, y=ingoing)
                return

            current_vertex = current_vertex.x
            index += 1

    def __repr__(self):
        return f'DirectedGraph({self.head})'


class Vertex:
    __slots__ = ('data', 'x', 'y')
    def __init__(self, index: int, data=None, x=None, y=None):
        self.data = data
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.data}, {self.x}, {self.y})'
