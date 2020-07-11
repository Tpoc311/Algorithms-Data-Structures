from LinkedList import *

lst = LinkedList()

# Check push_back
lst.push_back(0)
lst.push_back(1)
lst.push_back(2)

# Check pop_back
lst.pop_back()
lst.pop_back()
lst.pop_back()

# Check push_front
lst.push_front(-3)
lst.push_front(-2)
lst.push_front(-1)

# Check pop_front
lst.pop_front()
lst.pop_front()
lst.pop_front()

# Check insert
lst.insert(0, 0)
lst.insert(0, -1)
lst.insert(2, 1)
lst.insert(3, 2)
lst.insert(5, 2)

# Check removeAt
lst.removeAt(0)
lst.removeAt(0)
lst.removeAt(1)
lst.removeAt(2)

# Check get_size
size = lst.get_size()

# Check clear
lst.clear()
lst.clear()
