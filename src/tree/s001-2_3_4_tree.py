# -*- coding: utf-8 -*-

# 2-3-4 tree 是一个 4 阶树，这里的阶可以理解为结点的最大子结点数
# 是由 2结点、3结点、4结点组成的平衡树
# 2结点 一个结点可以有一个元素，2个子结点
# 3结点 一个结点可以有两个元素，3个子结点
# 4结点 一个结点可以有三个元素，4个子结点

# 插入
# 插入结点低于4结点，直接插入
#        属于4结点，结点发生裂变，中间元素移入父结点，剩余元素裂变为2个子结点，
# 然后将元素插入某一子结点，对于中间元素移入父结点就相当于一次对父结点的插入

# 类比 红黑树
#          8     ->     12                                       12（黑）
#   4 -> 6     9 -> 10      15 -> 19 -> 22       8（红）                          19（黑）
#                                        6（黑）          10（黑）        15（红）              22（红）
#                                     4（红）          9（红）
#


class Node:
    def __init__(self, elements=[], parent=None, sub_nodes=[]):
        if elements is None:
            elements = []
        self.elements = elements

        self.parent = parent

        if sub_nodes is None:
            sub_nodes = []
        self.sub_nodes = sub_nodes


def search(tree_node, val):
    if tree_node.elements:
        for i in range(len(tree_node.elements)):
            if tree_node.elements[i] > val:
                if i < len(tree_node.sub_tree_nodes):
                    tree_node = tree_node.sub_nodes[i]
                    return search(tree_node, val)
                else:
                    return tree_node
            if tree_node.elements[i] < val:
                if i + 1 < len(tree_node.sub_tree_nodes):
                    tree_node = tree_node.sub_nodes[i + 1]
                    return search(tree_node, val)
                else:
                    return tree_node
            if tree_node.elements[i] == val:
                return tree_node
    return tree_node


def insert(tree_node, val):
    tree_node = search(tree_node, val)
    if len(tree_node.elements) < 3:
        for i in range(len(tree_node.elements)):
            if tree_node.elements[i] >= val:
                tree_node.elements = tree_node.elements[0:i] + [val] + tree_node.elements[i:len(tree_node.elements)]
            if tree_node.elements[i] < val and i == len(tree_node.elements) - 1:
                tree_node.elements = tree_node.elements[0:i] + [val]
    else:
        sub_1 = Node([tree_node.elements[0]])
        sub_2 = Node([tree_node.elements[2]])
        if val <= tree_node.elements[0]:
            node = Node()
            node.

        if tree_node.parent is None:
            parent = Node([tree_node.elements[1]], None, [sub_1, sub_2])
            return
        else:
            insert(tree_node.parent, tree_node.elements[1])





if __name__ == '__main__':
    node = Node([], None, [])


