class Queue:
    class QueueNode:
        def __init__(self, data):
            self.data = data
            self.next_node = None

        @property
        def next_node(self):
            return self.__next_node

        @next_node.setter
        def next_node(self, next_node):
            self.__next_node = next_node

        @property
        def data(self):
            return self.__data

        @data.setter
        def data(self, data):
            self.__data = data

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return True if not self.head else False

    def enqueue(self, data):
        new_node = Queue.QueueNode(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def dequeue(self):
        self.head = self.head.next_node

    def front(self):
        data = self.head.data
        self.head = self.head.next_node
        return data


class Stack:
    class StackNode:
        def __init__(self, data):
            self.data = data
            self.next_node = None

        @property
        def next_node(self):
            return self.__next_node

        @next_node.setter
        def next_node(self, next_node):
            self.__next_node = next_node

        @property
        def data(self):
            return self.__data

        @data.setter
        def data(self, data):
            self.__data = data

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return True if not self.head else False

    def push(self, data):
        new_node = Queue.QueueNode(data)
        new_node.next_node = self.head
        self.head = new_node

    def pop(self):
        data = self.head.data
        self.head = self.head.next_node
        return data


def stack_example():
    s = Stack()

    s.push(1)
    s.push(2)
    s.push(3)

    print(s.pop())
    print(s.pop())
    print(s.pop())


def queue_example():
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print(q.front())
    print(q.front())
    print(q.front())


if __name__ == "__main__":
    stack_example()
    queue_example()