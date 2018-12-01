arr = [
        {"priority": 10, "content": "10"},
        {"priority": 12, "content": "12"},
        {"priority": 8, "content": "8"},
        {"priority": 32, "content": "8"},
        {"priority": 24, "content": "8"},
        {"priority": 76, "content": "8"},
        {"priority": 24, "content": "8"}
]


def test_max_heap():
    
    heap = MinHeap({"priority": 20}, arr)


def test_min_heap():
    # heap = MaxHeap({"priority": 20}, arr)
    
    del_element = heap.pop()
    print del_element["priority"]

    element = {"priority": 89, "content": "10"}
    heap.push(element)

    del_element = heap.pop()
    print del_element["priority"]

    del_element = heap.pop()
    print del_element["priority"]

    del_element = heap.pop()
    print del_element["priority"]