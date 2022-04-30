"""
Singly Linked List implementation.

29.04.2022
"""
from typing import NoReturn


class Node:
    data = None
    next = None

    def __init__(self, data, next=None) -> NoReturn:
        """
        Initializes data and pointer to next node.

        :param data: value to put.
        :param next: pointer to next node.
        :return: NoReturn.
        """
        self.next = next
        self.data = data


class LinkedList:
    head = None
    size = None

    def __init__(self, data=None) -> NoReturn:
        """
        Initializes LinkedList with head element or with no elements.

        :param data: data for head element (if needed).
        :return: NoReturn
        """

        if data is not None:
            self.head = Node(data=data)
            self.size = 1
        else:
            self.head = None
            self.size = 0

    def push_front(self, data) -> NoReturn:
        """
        Adds new element to head of the the list.

        :param data: data for new Node.
        :return: NoReturn.
        """
        self.head = Node(data, self.head)
        self.size += 1

    def pop_front(self) -> Node:
        if not self._isListEmpty():
            toDelete = self.head
            self.head = toDelete.next
            toDelete.next = None
            self.size -= 1
            return toDelete
        else:
            return None

    def __isListEmpty__(self) -> bool:
        """
        Checks if the list is empty or not.
        :return: True if empty / False if not.
        """
        if self.head is None:
            return True
        else:
            return False

    def get_size(self):
        return self.size

    def clear(self):
        while self.size != 0:
            self.pop_front()
