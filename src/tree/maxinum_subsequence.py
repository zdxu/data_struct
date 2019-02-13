# -*- coding: utf-8 -*-

import random


def init_sequence(seq_len):
    sequence = []
    for i in range(seq_len):
        sequence.append(random.randint(-20, 20))
    return sequence


def maxinum_subsequence(sequence):
    maxinum = 0
    maxinum_index = 0
    maxinum_endex = 0
    temp = 0
    temp_index = 0
    temp_endex = 0
    for i in range(len(sequence)):
        if temp + sequence[i] < 0:
            temp_index = i + 1
            temp = 0
        else:
            if temp + sequence[i] > temp:
                temp_endex = i
            temp = temp + sequence[i]
            if temp > maxinum:
                maxinum = temp
                maxinum_index = temp_index
                maxinum_endex = temp_endex

    return maxinum, maxinum_index, maxinum_endex


if __name__ == '__main__':
    sequence = [-10,1,2,3,4,-5,-23,3,7,-21];#init_sequence(20)
    print sequence
    print maxinum_subsequence(sequence)
