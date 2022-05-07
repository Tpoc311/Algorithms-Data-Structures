import pytest

from data_structures.LinkedList import DLinkedList, SLinkedList


@pytest.mark.parametrize("llist_type, data, expected_result",
                         [(DLinkedList, None, 0), (DLinkedList, 10, 1), (DLinkedList, "111", 1),
                          (SLinkedList, None, 0), (SLinkedList, 10, 1), (SLinkedList, "111", 1)])
def test_dll_init(llist_type, data, expected_result):
    dll = llist_type(data=data)
    assert dll.__get_size__() == expected_result


@pytest.mark.parametrize("llist_type, data, expected_result", [(DLinkedList, 23, [23]), (DLinkedList, "111", ["111"]),
                                                               (SLinkedList, 23, [23]), (SLinkedList, "111", ["111"])])
def test_dll_push_front_when_empty(llist_type, data, expected_result):
    dll = llist_type()
    dll.push_front(data=data)
    assert dll.to_list() == expected_result


@pytest.mark.parametrize("llist_type, data_list, expected_result",
                         [(DLinkedList, [1, "111", 3, 4, 5], [5, 4, 3, "111", 1]),
                          (SLinkedList, [1, "111", 3, 4, 5], [5, 4, 3, "111", 1])])
def test_dll_push_front(llist_type, data_list, expected_result):
    dll = llist_type()
    for d in data_list:
        dll.push_front(data=d)
    assert dll.to_list() == expected_result


@pytest.mark.parametrize("llist_type, expected_result", [(DLinkedList, None),
                                                         (SLinkedList, None)])
def test_dll_pop_front_when_empty(llist_type, expected_result):
    dll = llist_type()
    assert dll.pop_front() == expected_result


@pytest.mark.parametrize("llist_type, data_list, expected_result",
                         [(DLinkedList, [1, 2, "111", 4, 5], [5, 4, "111", 2, 1]),
                          (SLinkedList, [1, 2, "111", 4, 5], [5, 4, "111", 2, 1])])
def test_dll_pop_front(llist_type, data_list, expected_result):
    dll = llist_type()
    for d in data_list:
        dll.push_front(data=d)

    result = []
    while dll.head is not None:
        result.append(dll.pop_front())
    assert result == expected_result


@pytest.mark.parametrize("llist_type, expected_result", [(DLinkedList, True),
                                                         (SLinkedList, True)])
def test_dll_pop_front_links(llist_type, expected_result):
    dll = llist_type(1)
    dll.pop_front()
    if type(llist_type) == DLinkedList:
        assert (dll.head is None) and (dll.tail is None) == expected_result
    else:
        assert (dll.head is None) == expected_result


@pytest.mark.parametrize("llist_type, data, expected_result", [(DLinkedList, 23, 23), (DLinkedList, "111", "111"),
                                                               (SLinkedList, 23, 23), (SLinkedList, "111", "111")])
def test_dll_push_back_when_empty(llist_type, data, expected_result):
    dll = llist_type()
    dll.push_back(data=data)
    assert dll.pop_front() == expected_result


@pytest.mark.parametrize("llist_type, data_list, expected_result",
                         [(DLinkedList, [1, "111", 3, 4, 5], [1, "111", 3, 4, 5]),
                          (SLinkedList, [1, "111", 3, 4, 5], [1, "111", 3, 4, 5])])
def test_dll_push_back(llist_type, data_list, expected_result):
    dll = llist_type()
    for d in data_list:
        dll.push_back(data=d)
    assert dll.to_list() == expected_result


@pytest.mark.parametrize("llist_type, expected_result", [(DLinkedList, None),
                                                         (SLinkedList, None)])
def test_dll_pop_back_when_empty(llist_type, expected_result):
    dll = llist_type()
    assert dll.pop_back() == expected_result


@pytest.mark.parametrize("llist_type, data_list, expected_result",
                         [  # (DLinkedList, [1, 2, "333", 4, 5], [5, 4, "333", 2, 1]),
                             (SLinkedList, [1, 2, "333", 4, 5], [5, 4, "333", 2, 1])])
def test_dll_pop_back(llist_type, data_list, expected_result):
    dll = llist_type()
    for d in data_list:
        dll.push_back(data=d)

    result = []
    while dll.head is not None:
        result.append(dll.pop_back())
    assert result == expected_result


@pytest.mark.parametrize("llist_type, expected_result", [(DLinkedList, True),
                                                         (SLinkedList, True)])
def test_dll_pop_back_links(llist_type, expected_result):
    dll = llist_type(1)
    dll.pop_back()

    if type(llist_type) == DLinkedList:
        assert (dll.head is None) and (dll.tail is None) == expected_result
    else:
        assert (dll.head is None) == expected_result


@pytest.mark.parametrize("llist_type, expected_result", [(DLinkedList, None),
                                                         (SLinkedList, None)])
def test_dll_push_when_empty(llist_type, expected_result):
    dll = llist_type()
    assert dll.insertAfter(index=0, data=1) == expected_result


@pytest.mark.parametrize("llist_type, data_list, index, expected_result",
                         [(DLinkedList, [1, 2, 3, "444"], 0, ["444", "444", 3, 2, 1, 3, 2, 1]),
                          (DLinkedList, [1, 2, 3, "444"], 2, ["444", 3, 2, "444", 3, 2, 1, 1]),
                          (SLinkedList, [1, 2, 3, "444"], 0, ["444", "444", 3, 2, 1, 3, 2, 1]),
                          (SLinkedList, [1, 2, 3, "444"], 0, ["444", "444", 3, 2, 1, 3, 2, 1])])
def test_dll_push(llist_type, data_list, index, expected_result):
    dll = llist_type()
    for d in data_list:
        dll.push_front(data=d)

    for data in data_list:
        dll.insertAfter(index=index, data=data)
    assert dll.to_list() == expected_result


@pytest.mark.parametrize("llist_type, index, expected_result",
                         [(DLinkedList, 0, None), (DLinkedList, 1, None), (DLinkedList, 10, None),
                          (SLinkedList, 0, None), (SLinkedList, 1, None), (SLinkedList, 10, None)
                          ])
def test_dll_pop_when_empty(llist_type, index, expected_result):
    dll = llist_type()
    assert dll.pop(index=index) == expected_result


@pytest.mark.parametrize("llist_type, data_list, index, expected_result",
                         [(DLinkedList, [1, 2, 3, "444"], 0, [2, 3, "444"]),
                          (DLinkedList, [1, 2, 3, "444"], 2, [1, 2, "444"]),
                          (DLinkedList, [1, 2, 3, "444"], 3, [1, 2, 3]),
                          (SLinkedList, [1, 2, 3, "444"], 0, [2, 3, "444"]),
                          (SLinkedList, [1, 2, 3, "444"], 2, [1, 2, "444"]),
                          (SLinkedList, [1, 2, 3, "444"], 3, [1, 2, 3])])
def test_dll_pop(llist_type, data_list, index, expected_result):
    dll = llist_type()
    for d in data_list:
        dll.push_back(data=d)

    dll.pop(index=index)
    assert dll.to_list() == expected_result


@pytest.mark.parametrize("llist_type, index, expected_result",
                         [(DLinkedList, 0, None), (DLinkedList, 1, None), (DLinkedList, 10, None),
                          (SLinkedList, 0, None), (SLinkedList, 1, None), (SLinkedList, 10, None)])
def test_dll_get_when_empty(llist_type, index, expected_result):
    dll = llist_type()
    assert dll.get(index=index) == expected_result


@pytest.mark.parametrize("llist_type, data_list, index, expected_result", [(DLinkedList, [1, 2, 3, "444"], 0, 1),
                                                                           (DLinkedList, [1, 2, 3, "444"], 2, 3),
                                                                           (DLinkedList, [1, 2, 3, "444"], 3, "444"),
                                                                           (SLinkedList, [1, 2, 3, "444"], 0, 1),
                                                                           (SLinkedList, [1, 2, 3, "444"], 2, 3),
                                                                           (SLinkedList, [1, 2, 3, "444"], 3, "444")])
def test_dll_get(llist_type, data_list, index, expected_result):
    dll = llist_type()
    for d in data_list:
        dll.push_back(data=d)

    assert dll.get(index=index) == expected_result
