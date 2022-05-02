# Implementation of common Data Structures

Here are implementation of common data structures presented.

## Linked List

In this implementation we use two classes - `Node` and `LinkedList`.

### Node class

The `Node` class is a data class used to store each value. `Node` class has two attributes:

1. `data` - to store value of the node.
2. `next` - pointer to next node.

### LinkedList class

`LinkedList` class used to operate on each node.

Attributes:

1. `head` - pointer to first value in the list.
2. `size` - number of elements stored in the list

Methods implemented for LinkedList:

1. `push_front` - Inserts new node in front of the list.
![alt text](https://github.com/Tpoc311/Algorithms-Data-Structures/Python/images/LinkedList/push_front.png)
2. `pop_front` - Removes first node of the list and returns its data.
3. `push` - Inserts new node after node with given index.
4. `pop` - Removes node after node with given index and returns its data.
5. `push_back` - Inserts new node into tail of the list.
6. `pop_back` - Removes last node of the list and returns its data.
7. `to_list` - Converts the LinkedList to list.
8. `clear` - Removes list.
9. `__isListEmpty__` - Checks if the list is empty or not.
10. `__searchByIndex__` - Searches node with given index.
11. `__get_size__` - Returns size of the list.