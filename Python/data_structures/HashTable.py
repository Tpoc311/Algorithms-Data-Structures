"""
Implementation of hash-table. The hash-table stores (key, value) pairs.
Collision resolve method: chaining.
Data structure: list of lists (Python list is technically dynamic array).
30.04.2022

V.S. Kolesnikov
"""

from typing import NoReturn, Any


class HashTable:
    def __init__(self, size=2048):
        self.arr_size = size
        self.table = [[] for _ in range(self.arr_size)]

    def insert(self, key: Any, value: Any) -> NoReturn:
        """
        Inserts new (key, value) pair into Hash-Table.

        :param key: key to be inserted.
        :param value: value to be inserted.
        :return: NoReturn.
        """
        hash_table_idx = hash(key) % self.arr_size

        isKeyExists, list_idx = self.__isKeyExists__(key, hash_table_idx)
        if isKeyExists:
            self.table[hash_table_idx][list_idx] = (key, value)
        else:
            self.table[hash_table_idx].append((key, value))

    def traverse(self) -> NoReturn:
        """
        Traverses hash-table and prints every element in order which elements are stored.
        :return: NoReturn.
        """
        for lst in self.table:
            for i in lst:
                print(i)

    def remove(self, key: Any) -> NoReturn:
        """
        Searches and removes element by given key.
        :param key: key to look for.
        :return: NoReturn
        """
        hash_table_idx = hash(key) % self.arr_size

        isKeyExists, list_idx = self.__isKeyExists__(key, hash_table_idx)
        if isKeyExists:
            del self.table[hash_table_idx][list_idx]

    def search(self, key: Any):
        hash_table_idx = hash(key) % self.arr_size

        isKeyExists, list_idx = self.__isKeyExists__(key, hash_table_idx)
        if isKeyExists:
            return self.table[hash_table_idx][list_idx]

    def __isKeyExists__(self, key: Any, hash_table_idx) -> (bool, int):
        """
        Checks if given key exists in hash_table_idx list.

        :param key: key to check.
        :param hash_table_idx: index for list located by hash_table_idx index.
        :return: pair (<if key exists>, <index of this key in list>).
        """
        for list_idx, kv in enumerate(self.table[hash_table_idx]):
            in_list_key, _ = kv
            if in_list_key == key:
                return True, list_idx
        return False, None
