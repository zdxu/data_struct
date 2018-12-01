# -*- coding: utf-8 -*-

import math


class MinHeap:
    def __init__(self, sentinel, arr=[]):
        self.data = [sentinel] + arr
        arr_length = len(arr)
        if arr_length > 2:
            tree_height = int(math.floor(math.log(arr_length-1, 2)))
            i = tree_height
            while i >= 1:
                for idx in range(pow(2, i - 1), pow(2, i)):
                    self.__compare_and_swap(idx, idx * 2, idx * 2 + 1)
                i = i - 1

    def __compare_and_swap(self, idx, left_node_idx, right_node_idx):
        if left_node_idx >= len(self.data):
            return 

        node = self.data[idx]
        min_node_idx = left_node_idx
        min_node = self.data[left_node_idx]
        if right_node_idx < len(self.data):
            right_node = self.data[right_node_idx]
            if right_node["priority"] < min_node["priority"]:
                min_node = right_node
                min_node_idx = right_node_idx
        if min_node["priority"] < node["priority"]:
            self.data[idx] = min_node
            self.data[min_node_idx] = node
            self.__compare_and_swap(min_node_idx, min_node_idx * 2, min_node_idx * 2 + 1)

    def push(self, node):
        self.data.append(node)
        idx = len(self.data) - 1
        while idx > 1:
            parent_idx = idx // 2
            parent_node = self.data[parent_idx]
            node = self.data[idx]
            if node["priority"] >= parent_node["priority"]:
                break
            else:
                self.data[idx] = parent_node
                self.data[parent_idx] = node
                idx = parent_idx
    
    def pop(self):
        idx = 1
        node = self.data[idx]
        self.data[idx] = self.data[len(self.data) - 1]
        del self.data[len(self.data) - 1]
        self.__compare_and_swap(idx, idx * 2, idx * 2 + 1)
        return node


