class LinkedList:
    head = None
    size = None

    def __init__(self):
        self.head = None
        self.size = 0

    def push_back(self, value):
        # Add an item to the end of the list.
        if self.size == 0:
            self.head = Node(value, None)
            self.size += 1
        else:
            self.insert(self.size, value)

    def pop_back(self):
        # Remove the back item of the list.
        return self.removeAt(self.size - 1)

    def push_front(self, value):
        # Add item to the front of the list.
        self.head = Node(value, self.head)
        self.size += 1

    def pop_front(self):
        # Remove the first item from the list.
        if self.head is None:
            return None
        else:
            toDelete = self.head
            self.head = toDelete.pNext
            toDelete.pNext = None
            self.size -= 1
            return toDelete

    def insert(self, index, value):
        # Insert an item at a given index.
        if self.size == 0:
            self.push_front(value)
        elif index > self.size:
            return None
        elif index == 0:
            toInsert = Node(value, self.head)
            self.head = toInsert
            self.size += 1
        else:
            previous = self.head
            for i in range(0, index - 1):
                previous = previous.pNext
            toInsert = Node(value, previous.pNext)
            previous.pNext = toInsert
            self.size += 1

    def removeAt(self, index):
        # Remove an item from a given index.
        if index == 0:
            return self.pop_front()
        elif index > self.size:
            return None
        elif self.size == 0:
            return None
        else:
            previous = self.head
            for i in range(0, index - 1):
                previous = previous.pNext
            toDelete = previous.pNext
            previous.pNext = toDelete.pNext
            self.size -= 1
            return toDelete

    def get_size(self):
        return self.size

    def clear(self):
        while self.size != 0:
            self.pop_front()


class Node:
    pNext = None
    data = None

    def __init__(self, value, pNext):
        self.pNext = pNext
        self.data = value
