class Stack:
    def __init__(self):
        self.queue = []
    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        self.queue.append(x)

    """
    @return: nothing
    """
    def pop(self):
        return self.queue.pop()

    """
    @return: An integer
    """
    def top(self):
        return self.queue[-1]

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        return self.queue == []
