# -*- coding: utf-8 -*-

from src.tree.heap.max_heap import MaxHeap


def test_max_heap():

    arr = [{
        "priority": 10,
        "content": "10"
    }, {
        "priority": 12,
        "content": "12"
    }, {
        "priority": 8,
        "content": "8"
    }, {
        "priority": 32,
        "content": "8"
    }, {
        "priority": 24,
        "content": "8"
    }, {
        "priority": 76,
        "content": "8"
    }, {
        "priority": 24,
        "content": "8"
    }]

    heap = MaxHeap({"priority": 20}, arr)

    max_priority = max_priority_get(arr)
    element = heap.pop()
    assert element["priority"] == max_priority

    element = {"priority": 101, "content": "101"}
    heap.push(element)
    assert element["priority"] == heap.pop()["priority"]


def max_priority_get(arr):
    max_priority = 0
    for item in arr:
        if max_priority < item["priority"]:
            max_priority = item["priority"]
    return max_priority
