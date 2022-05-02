"""
Singly Linked List implementation.

29.04.2022
"""
from typing import NoReturn


class Node:
    data = None
    next = None

    def __init__(self, data: Any, next=None) -> NoReturn:
        """
        Initializes data and pointer to next node.
        :param data: data for new node.
        :param next: pointer to next node.
        :return: NoReturn.
        """
        self.next = next
        self.data = data


class LinkedList:
    head = None
    size = None

    def __init__(self, data: Any = None) -> NoReturn:
        """
        Initializes LinkedList with head element or with no elements.
        :param data: data for head element (if needed).
        :return: NoReturn.
        """
        if data is not None:
            self.push_front(data=data)
            self.size = 1
        else:
            self.head = None

    def push_front(self, data: Any) -> NoReturn:
        """
        Inserts new node in front of the the list.
        :param data: data for new node.
        :return: NoReturn.
        """
        self.head = Node(data, self.head)
        self.size += 1

    def pop_front(self) -> Any:
        """
        Removes first node of the list and returns its data.
        :return: data of first node.
        """
        if not self.__isListEmpty__():
            tmp = self.head
            self.head = tmp.next
            self.size -= 1
            return tmp.data
        else:
            return None

    def __isListEmpty__(self) -> bool:
        """
        Checks if the list is empty or not.
        :return: True if empty / False if not.
        """
        if self.__get_size__() == 0:
            return True
        else:
            return False

    def get_size(self):
        return self.size
