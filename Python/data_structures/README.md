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

* `push_front` - Inserts new node in front of the list.
    1. Create new node.
    2. Link new node to head node.
    3. Point head to new node.

  ![push_front](https://github.com/Tpoc311/Algorithms-Data-Structures/blob/master/Python/images/LinkedList/push_front.png "Push front illustration")

* `pop_front` - Removes first node of the list and returns its data.

    1. Link head node to next node.
    2. Remove first node.

  Note: if you use python3 you can skip step 2 cause garbage collector will remove inaccessible node.

  ![pop_front](https://github.com/Tpoc311/Algorithms-Data-Structures/blob/master/Python/images/LinkedList/pop_front.png "Pop front illustration")

* `push` - Inserts new node after node with given index (N-th node).
    1. Create new node.
    2. Link new node to node which is next to N-th node.
    3. Link N-th node to new node.

  ![push](https://github.com/Tpoc311/Algorithms-Data-Structures/blob/master/Python/images/LinkedList/push.png "Push illustration")

* `pop` - Removes node after node with given index and returns its data (N-th node).
    1. Link N-th node to node after next node.
    2. Remove node next to N-th node.

  Note: if you use python3 you can skip step 2 cause garbage collector will remove inaccessible node.

  ![pop](https://github.com/Tpoc311/Algorithms-Data-Structures/blob/master/Python/images/LinkedList/pop.png "Pop illustration")

* `push_back` - Inserts new node into tail of the list.
    1. Create new node.
    2. Link last node to new node.

  ![push_back](https://github.com/Tpoc311/Algorithms-Data-Structures/blob/master/Python/images/LinkedList/push_back.png "Push back illustration")

* `pop_back` - Removes last node of the list and returns its data.
    1. Link node before last node to None (Null).
    2. Remove last node.

  Note: if you use python3 you can skip step 2 cause garbage collector will remove inaccessible node.

  ![pop_back](https://github.com/Tpoc311/Algorithms-Data-Structures/blob/master/Python/images/LinkedList/pop_back.png "Pop back illustration")

* `to_list` - Converts the LinkedList to list.
* `clear` - Removes list.
* `__isListEmpty__` - Checks if the list is empty or not.
* `__searchByIndex__` - Searches node with given index.
* `__get_size__` - Returns size of the list.

For `push`, `pop`, `push_back` and `pop_back` operations you first need iterate till N-th node.