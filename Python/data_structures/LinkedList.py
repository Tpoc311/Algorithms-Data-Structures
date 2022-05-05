"""
Singly and Doubly Linked List implementation.

Computational complexity of Doubly Linked List:
push_front - O(1)
pop_front - O(1)
push - O(N)
pop - O(N)
push_back - O(1)
pop_back - O(1)
is_data_in_list - O(N)
get - O(N)

Computational complexity of Singly Linked List:
push_front - O(1)
pop_front - O(1)
push - O(N)
pop - O(N)
push_back - O(N)
pop_back - O(N)
get - O(N)

Author: V.S. Kolesnikov.
Edit date: 05.05.2022.
"""
from typing import NoReturn, Any, List


class DNode:
    data = None
    next = None
    prev = None

    def __init__(self, data: Any, next=None, prev=None) -> NoReturn:
        """
        Initializes data and pointer to next node.
        :param data: data for new node.
        :param next: pointer to next node.
        :return: NoReturn.
        """
        self.data = data
        self.next = next
        self.prev = prev


class DLinkedList:
    head = None
    tail = None
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

    def push_front(self, data: Any) -> NoReturn:
        """
        Inserts new node in front of the the list.
        :param data: data for new node.
        :return: NoReturn.
        """
        if self.__isListEmpty__():
            self.tail = self.head = DNode(data=data)
        else:
            self.head = DNode(data=data, next=self.head)
            self.head.next.prev = self.head
        self.size += 1

    def pop_front(self) -> Any:
        """
        Removes first node of the list and returns its data.
        :return: data of first node.
        """
        if not self.__isListEmpty__():
            toPop = self.head.data
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
            return toPop

    def push(self, index: int, data: Any) -> NoReturn:
        """
        Inserts new node after node with given index.
        :param index: node index to insert after.
        :param data: data for new Node.
        :return: NoReturn
        """
        if index == self.__get_size__() - 1:
            self.push_back(data=data)
            return

        node_by_index = self.__searchByIndex__(index=index)
        if node_by_index is not None:
            new_node = DNode(data=data, next=node_by_index.next, prev=node_by_index)
            node_by_index.next = new_node
            new_node.next.prev = new_node
            self.size += 1

    def pop(self, index: int) -> Any:
        """
        Removes node with given index and returns its data.
        :param index: node index to remove.
        :return: data of Node with given index.
        """
        if index == self.__get_size__() - 1:
            self.pop_back()
            return

        node_by_index = self.__searchByIndex__(index=index)
        if node_by_index is not None:
            toPop = node_by_index.data
            node_by_index.prev.next = node_by_index.next
            node_by_index.next.prev = node_by_index.prev
            self.size -= 1
            return toPop

    def push_back(self, data: int) -> NoReturn:
        """
        Inserts new node into tail of the list.
        :param data: data for new Node.
        :return: NoReturn.
        """
        if self.__isListEmpty__():
            self.tail = self.head = DNode(data=data)
        else:
            self.tail.next = DNode(data=data, prev=self.tail)
            self.tail = self.tail.next
        self.size += 1

    def pop_back(self) -> Any:
        """
        Removes last node of the list and returns its data.
        :return: data of last Node.
        """
        if not self.__isListEmpty__():
            toPop = self.tail.data
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
            return toPop

    def is_data_in_list(self, data: Any) -> int:
        """
        Checks if given value already in list and returns its index.
        :param data: value to check.
        :return: index of found value.
        """
        current = self.head
        counter = 0
        while current is not None:
            if current.data == data:
                return counter
            current = current.next
            counter += 1

    def get(self, index: int) -> Any:
        """
        Searches value in list by given index and returns it.
        :param index: index to look for.
        :return: data by given index.
        """
        node_by_index = self.__searchByIndex__(index=index)
        return node_by_index.data

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

    def __searchByIndex__(self, index: int) -> DNode:
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


from typing import NoReturn, Any, List


class SNode:
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


class SLinkedList:
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
        self.head = SNode(data, self.head)
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
            new_node = SNode(data=data)
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

    def get(self, index: int) -> Any:
        """
        Searches value in list by given index and returns it.
        :param index: index to look for.
        :return: data by given index.
        """
        node_by_index = self.__searchByIndex__(index=index)
        return node_by_index.data

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

    def __searchByIndex__(self, index: int) -> SNode:
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
