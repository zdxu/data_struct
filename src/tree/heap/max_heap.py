# -*- coding: utf-8 -*-

import math


def test():
    pass


class MaxHeap:
    def __init__(self, sentinel, arr=[]):
        self.__data = [sentinel] + arr
        arr_length = len(arr)
        if arr_length > 2:
            tree_height = int(math.floor(math.log(arr_length - 1, 2)))
            i = tree_height
            while i >= 1:
                for idx in range(pow(2, i - 1), pow(2, i)):
                    self.__compare_and_swap(idx, idx * 2, idx * 2 + 1)
                i = i - 1

    def __compare_and_swap(self, idx, left_node_idx, right_node_idx):
        if left_node_idx >= len(self.__data):
            return

        node = self.__data[idx]
        max_node_idx = left_node_idx
        max_node = self.__data[left_node_idx]
        if right_node_idx < len(self.__data):
            right_node = self.__data[right_node_idx]
            if right_node["priority"] > max_node["priority"]:
                max_node = right_node
                max_node_idx = right_node_idx
        if max_node["priority"] > node["priority"]:
            self.__data[idx] = max_node
            self.__data[max_node_idx] = node
            self.__compare_and_swap(max_node_idx, max_node_idx * 2,
                                    max_node_idx * 2 + 1)

    def push(self, node):
        self.__data.append(node)
        idx = len(self.__data) - 1
        while idx > 1:
            parent_idx = idx // 2
            parent_node = self.__data[parent_idx]
            node = self.__data[idx]
            if node["priority"] <= parent_node["priority"]:
                break
            else:
                self.__data[idx] = parent_node
                self.__data[parent_idx] = node
                idx = parent_idx

    def pop(self):
        idx = 1
        node = self.__data[idx]
        self.__data[idx] = self.__data[len(self.__data) - 1]
        del self.__data[len(self.__data) - 1]
        self.__compare_and_swap(idx, idx * 2, idx * 2 + 1)
        return node