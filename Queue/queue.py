class Queue:
    __slots__ = ('queue')
    def __init__(self, queue=[]):
        self.queue = list(queue)

    def enqueue(self, item):
        """Function to insert item to queue"""
        self.queue.append(item)

    def dequeue(self):
        """Function to remove and return last element from queue"""
        if self.isEmpty():
            return None
        return self.queue.pop(0)

    def top(self):
        """Function to return last element from queue without remove"""
        if self.isEmpty():
            return None
        return self.queue[0]

    def isEmpty(self):
        """Function to check is queue empty"""
        return len(self.queue) == 0

    def __iadd__(self, other):
        """Function to add element to queue and asign a value to queue. Return self"""
        try:
            self.queue += other.queue
            return self
        except AttributeError:
            self.push(other)
            return self

    def __add__(self, other):
        """Function to add element to queue and return value"""
        try:
            if type(other) == list:
                return Queue(self.queue + other)
            return Queue(self.queue + other.queue)
        except AttributeError:
            print(other)
            return Queue(self.queue + list(other))

    def __len__(self):
        """Function to get queue lenght"""
        return len(self.queue)

    def __repr__(self):
        """Function to print self"""
        return f'Queue({self.queue})'
