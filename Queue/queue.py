class Queue:
    __slots__ = ('queue')
    def __init__(self, queue=[]):
        self.queue = list(queue)

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if not len(self.queue):
            return None
        return self.queue.pop(0)

    def __iadd__(self, other):
        try:
            self.queue += other.queue
            return self
        except AttributeError:
            self.push(other)
            return self

    def __add__(self, other):
        try:
            if type(other) == list:
                return Queue(self.queue + other)
            return Queue(self.queue + other.queue)
        except AttributeError:
            print(other)
            return Queue(self.queue + list(other))

    def __len__(self):
        return len(self.queue)

    def __repr__(self):
        return f'Queue({self.queue})'
