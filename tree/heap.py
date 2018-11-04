import math


class MaxHeap:

    def __init__(self, sentinel, arr=[]):
        self.data = [sentinel] + arr
        if len(arr) > 1:
            height = int(math.floor(math.log(len(arr)-1, 2)))
            print height
            for idx in range(pow(2, height-1), pow(2, height)):
                print idx
                while idx > 0:
                    self.__compare_and_swap(idx, idx*2, idx*2 + 1)
                    idx = idx // 2
                    

    def __compare_and_swap(self,idx, sub_left_idx, sub_right_idx):
            sub_left_priority = self.data[idx]["priority"]
            sub_right_priority = self.data[idx]["priority"]
            if sub_left_idx < len(self.data) and sub_right_idx >= len(self.data):
                sub_left_priority = self.data[sub_left_idx]["priority"]
            if sub_right_idx < len(self.data):
                sub_left_priority = self.data[sub_left_idx]["priority"]
                sub_right_priority = self.data[sub_right_idx]["priority"]
            if sub_left_priority >= sub_right_priority:
                temp_idx = sub_left_idx
                temp_priority = sub_left_priority
            else:
                temp_idx = sub_right_idx
                temp_priority = sub_right_priority
            if self.data[idx]["priority"] < temp_priority:
                temp = self.data[idx]
                self.data[idx] = self.data[temp_idx]
                self.data[temp_idx] = temp
                return idx
            return temp_idx

    def add(self, element):
        self.data.append(element)
        idx = len(self.data) - 1
        if idx > 1:
            while(self.data[idx]["priority"] > self.data[idx//2]["priority"]):
                temp = self.data[idx]
                self.data[idx] = self.data[idx//2]
                self.data[idx//2] = temp
                idx = idx // 2

    def delete(self):
        if len(self.data) <= 1:
            raise "heap is empty"
        ret = self.data[1]
        self.data[1] = self.data[len(self.data)-1]
        del self.data[len(self.data)-1]
        idx = 1
        while idx < len(self.data):
            temp_idx = self.__compare_and_swap(idx, idx*2, idx*2+1)
            if temp_idx > idx:
                idx = temp_idx
            else:
                break
        return ret


class MinHeap(object):

    def __init__(self, sentinel, arr=[]):
        self.data = [sentinel] + arr
        if len(arr) > 1:
            height = int(math.floor(math.log(len(arr)-1, 2)))
            print height
            for idx in range(pow(2, height-1), pow(2, height)):
                print idx
                while idx > 0:
                    self.__compare_and_swap(idx, idx*2, idx*2 + 1)
                    idx = idx // 2
                    

    def __compare_and_swap(self,idx, sub_left_idx, sub_right_idx):
            sub_left_priority = self.data[idx]["priority"]
            sub_right_priority = self.data[idx]["priority"]
            if sub_left_idx < len(self.data) and sub_right_idx >= len(self.data):
                sub_left_priority = self.data[sub_left_idx]["priority"]
            if sub_right_idx < len(self.data):
                sub_left_priority = self.data[sub_left_idx]["priority"]
                sub_right_priority = self.data[sub_right_idx]["priority"]
            if sub_left_priority <= sub_right_priority:
                temp_idx = sub_left_idx
                temp_priority = sub_left_priority
            else:
                temp_idx = sub_right_idx
                temp_priority = sub_right_priority
            if self.data[idx]["priority"] > temp_priority:
                temp = self.data[idx]
                self.data[idx] = self.data[temp_idx]
                self.data[temp_idx] = temp
                return idx
            return temp_idx

    def add(self, element):
        self.data.append(element)
        idx = len(self.data) - 1
        if idx > 1:
            while(self.data[idx]["priority"] < self.data[idx//2]["priority"]):
                temp = self.data[idx]
                self.data[idx] = self.data[idx//2]
                self.data[idx//2] = temp
                idx = idx // 2

    def delete(self):
        if len(self.data) <= 1:
            raise "heap is empty"
        ret = self.data[1]
        self.data[1] = self.data[len(self.data)-1]
        del self.data[len(self.data)-1]
        idx = 1
        while idx < len(self.data):
            temp_idx = self.__compare_and_swap(idx, idx*2, idx*2+1)
            if temp_idx > idx:
                idx = temp_idx
            else:
                break
        return ret


if __name__ == '__main__':
    arr = [
        {"priority": 10, "content": "10"},
        {"priority": 12, "content": "12"},
        {"priority": 8, "content": "8"},
    ]

    # heap = MaxHeap({"priority": 20}, arr)
    heap = MinHeap({"priority": 20}, arr)

    del_element = heap.delete()
    print del_element["priority"]

    element = {"priority": 14, "content": "10"}
    heap.add(element)

    del_element = heap.delete()
    print del_element["priority"]

    del_element = heap.delete()
    print del_element["priority"]

    del_element = heap.delete()
    print del_element["priority"]
