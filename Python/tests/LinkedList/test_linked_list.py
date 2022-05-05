import pytest

from data_structures.LinkedList import DLinkedList


@pytest.mark.parametrize("data, expected_result", [(None, 0), (10, 1), ("111", 1)])
def test_dll_init(data, expected_result):
    dll = DLinkedList(data=data)
    assert dll.__get_size__() == expected_result


@pytest.mark.parametrize("data, expected_result", [(23, [23]), ("111", ["111"])])
def test_dll_push_front_when_empty(data, expected_result):
    dll = DLinkedList()
    dll.push_front(data=data)
    assert dll.to_list() == expected_result


@pytest.mark.parametrize("data_list, expected_result", [([1, "111", 3, 4, 5], [5, 4, 3, "111", 1])])
def test_dll_push_front(data_list, expected_result):
    dll = DLinkedList()
    for d in data_list:
        dll.push_front(data=d)
    assert dll.to_list() == expected_result


@pytest.mark.parametrize("expected_result", [None])
def test_dll_pop_front_when_empty(expected_result):
    dll = DLinkedList()
    assert dll.pop_front() == expected_result


@pytest.mark.parametrize("data_list, expected_result", [([1, 2, "111", 4, 5], [5, 4, "111", 2, 1])])
def test_dll_pop_front(data_list, expected_result):
    dll = DLinkedList()
    for d in data_list:
        dll.push_front(data=d)

    result = []
    while dll.head is not None:
        result.append(dll.pop_front())
    assert result == expected_result


@pytest.mark.parametrize("expected_result", [True])
def test_dll_pop_front_links(expected_result):
    dll = DLinkedList(1)
    dll.pop_front()
    assert (dll.head is None) and (dll.tail is None) == expected_result


@pytest.mark.parametrize("data, expected_result", [(23, 23), ("111", "111")])
def test_dll_push_back_when_empty(data, expected_result):
    dll = DLinkedList()
    dll.push_back(data=data)
    assert dll.pop_front() == expected_result


@pytest.mark.parametrize("data_list, expected_result", [([1, "111", 3, 4, 5], [1, "111", 3, 4, 5])])
def test_dll_push_back(data_list, expected_result):
    dll = DLinkedList()
    for d in data_list:
        dll.push_back(data=d)
    assert dll.to_list() == expected_result


@pytest.mark.parametrize("expected_result", [None])
def test_dll_pop_back_when_empty(expected_result):
    dll = DLinkedList()
    assert dll.pop_back() == expected_result


@pytest.mark.parametrize("data_list, expected_result", [([1, 2, "333", 4, 5], [5, 4, "333", 2, 1])])
def test_dll_pop_back(data_list, expected_result):
    dll = DLinkedList()
    for d in data_list:
        dll.push_back(data=d)

    result = []
    while dll.head is not None:
        result.append(dll.pop_back())
    assert result == expected_result


@pytest.mark.parametrize("expected_result", [True])
def test_dll_pop_back_links(expected_result):
    dll = DLinkedList(1)
    dll.pop_back()
    assert (dll.head is None) and (dll.tail is None) == expected_result


@pytest.mark.parametrize("expected_result", [None])
def test_dll_push_when_empty(expected_result):
    dll = DLinkedList()
    assert dll.push(index=0, data=1) == expected_result


@pytest.mark.parametrize("data_list, index, expected_result", [([1, 2, 3, "444"], 0, ["444", "444", 3, 2, 1, 3, 2, 1]),
                                                               ([1, 2, 3, "444"], 2, ["444", 3, 2, "444", 3, 2, 1, 1])])
def test_dll_push(data_list, index, expected_result):
    dll = DLinkedList()
    for d in data_list:
        dll.push_front(data=d)

    for data in data_list:
        dll.push(index=index, data=data)
    assert dll.to_list() == expected_result


@pytest.mark.parametrize("index, expected_result", [(0, None), (1, None), (10, None)])
def test_dll_pop_when_empty(index, expected_result):
    dll = DLinkedList()
    assert dll.pop(index=index) == expected_result


@pytest.mark.parametrize("data_list, index, expected_result", [([1, 2, 3, "444"], 0, [2, 3, "444"]),
                                                               ([1, 2, 3, "444"], 2, [1, 2, "444"]),
                                                               ([1, 2, 3, "444"], 3, [1, 2, 3])])
def test_dll_pop(data_list, index, expected_result):
    dll = DLinkedList()
    for d in data_list:
        dll.push_back(data=d)

    dll.pop(index=index)
    assert dll.to_list() == expected_result


@pytest.mark.parametrize("index, expected_result", [(0, None), (1, None), (10, None)])
def test_dll_get_when_empty(index, expected_result):
    dll = DLinkedList()
    assert dll.get(index=index) == expected_result


@pytest.mark.parametrize("data_list, index, expected_result", [([1, 2, 3, "444"], 0, 1),
                                                               ([1, 2, 3, "444"], 2, 3),
                                                               ([1, 2, 3, "444"], 3, "444")])
def test_dll_get(data_list, index, expected_result):
    dll = DLinkedList()
    for d in data_list:
        dll.push_back(data=d)

    assert dll.get(index=index) == expected_result
