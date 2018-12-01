# -*- coding: utf-8 -*-
import pytest
from src.tree.heap.min_heap import MinHeap

arr = None


@pytest.yield_fixture(scope="module")
def setup():
    global arr
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
    print("before every method execute")
    yield
    print("after every method execute")
    arr = None


@pytest.mark.usefixtures("setup")
def test_min_heap():
    heap = MinHeap({"priority": 20}, arr)

    min_priority = min_priority_get(arr)
    assert min_priority == heap.pop()["priority"]

    element = {"priority": 1, "content": "8"}
    heap.push(element)
    assert element["priority"] == heap.pop()["priority"]


def min_priority_get(arr):
    min_priority = arr[0]["priority"]
    for item in arr:
        if min_priority > item["priority"]:
            min_priority = item["priority"]
    return min_priority