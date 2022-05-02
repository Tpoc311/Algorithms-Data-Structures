"""
Singly Linked List implementation.

02.05.2022
"""
from typing import NoReturn, Any, List


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
    size = 0

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
            data_to_return = self.head
            self.head = self.head.next
            self.size -= 1
            return data_to_return
        else:
            return None

    def push(self, index: int, data: Any) -> NoReturn:
        """
        Inserts new node after node with given index.
        :param index: node index to insert after.
        :param data: data for new Node.
        :return: NoReturn
        """
        node_by_index = self.__searchByIndex__(index=index)
        if node_by_index is not None:
            new_node = Node(data=data)
            new_node.next = node_by_index.next
            node_by_index.next = new_node
            self.size += 1

    def pop(self, index: int) -> Any:
        """
        Removes node after node with given index and returns its data.
        :param index: node index to remove after.
        :return: data of Node after given index.
        """
        if self.__isListEmpty__():
            print("Error. List is empty.")
            return None

        node_by_index = self.__searchByIndex__(index=index)
        if node_by_index.next is None:
            print(f"Error. Node with index {index} is last node.")
            return

        if node_by_index is not None:
            toPop = node_by_index.next
            node_by_index.next = toPop.next
            self.size -= 1
            return toPop.data

    def push_back(self, data: int) -> NoReturn:
        """
        Inserts new node into tail of the list.
        :param data: data for new Node.
        :return: NoReturn.
        """
        self.push(index=self.__get_size__() - 1, data=data)

    def pop_back(self) -> Any:
        """
        Removes last node of the list and returns its data.
        :return: data of last Node.
        """
        return self.pop(index=self.__get_size__() - 2)

    def to_list(self) -> List[Any]:
        """
        Converts the LinkedList to list.
        :return: list of LinkedList elements.
        """
        lst = []
        current = self.head
        while current is not None:
            lst.append(current.data)
            current = current.next
        return lst

    def clear(self) -> NoReturn:
        """
        Removes list.
        :return: NoReturn.
        """
        self.head = None

    def __isListEmpty__(self) -> bool:
        """
        Checks if the list is empty or not.
        :return: True if empty / False if not.
        """
        if self.__get_size__() == 0:
            return True
        else:
            return False

    def __searchByIndex__(self, index: int) -> Node:
        """
        Searches node with given index.
        :param index: node index to search.
        :return: found node.
        """
        if self.__isListEmpty__():
            print("Error. List is empty.")
            return
        if index > self.size - 1:
            print(f"Error. Index of the last node is {self.size - 1}")
            return

        current = self.head
        counter = 0
        while current is not None:
            if counter == index:
                return current
            current = current.next
            counter += 1

    def __get_size__(self) -> int:
        """
        Returns size of the list.
        :return: size of list.
        """
        return self.size
