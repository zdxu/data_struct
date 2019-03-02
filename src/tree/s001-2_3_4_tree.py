# -*- coding: utf-8 -*-

# 2-3-4 tree 是一个 4 阶树，这里的阶可以理解为结点的最大子结点数
# 是由 2结点、3结点、4结点组成的平衡树
# 2结点 一个结点可以有一个元素，2个子结点
# 3结点 一个结点可以有两个元素，3个子结点
# 4结点 一个结点可以有三个元素，4个子结点

# 插入
# 若插入结点的父结点为4结点，则父结点先发生裂变，然后在将元素插入结点
# 插入结点低于4结点，直接插入
#        属于4结点，结点发生裂变，中间元素移入父结点，剩余元素裂变为2个子结点，
# 然后将元素插入某一子结点

# 删除元素
# 找到要删除元素，然后用其后继结点的最小元素对其进行替换，然后转换成删除其前继结点的最大元素删除
# 1、删除元素所在结点元素有多个，直接删除
# 2、删除元素所在结点只有一个元素，需要将其父级结点的大于它的最小元素移入至其右侧的第一个同级结点中，若无比它大的元素，则直接将父结点中的最
# 大元素移入其左侧的第一个同级结点中(等同于插入元素)，然后删除结点及其结点间关系，若父结点也只有一个结点，则按照同理进行处理。

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


class Tree:
    def __init__(self):
        self.root = None

    def search_node(self, val):
        node = self.search_near_node(val)
        if node:
            for element in node.elements:
                if element == val:
                    return node
        return None

    def search_near_node(self, val, sub_node=None):
        if sub_node is None:
            sub_node = self.root
        if sub_node.sub_nodes:
            for i in range(len(sub_node.elements)):
                if sub_node.elements[i] > val:
                    break
                if sub_node.elements[i] == val:
                    return sub_node
            if sub_node.elements[i] > val:
                sub_node = sub_node.sub_nodes[i]
                return self.search_near_node(val, sub_node)
            else:
                sub_node = sub_node.sub_nodes[i + 1]
                return self.search_near_node(val, sub_node)
        return sub_node

    @staticmethod
    def search_successor_node(val, node):
        if not node.sub_nodes:
            return node
        i = 0
        for element in node.elements:
            if element == val:
                break
            i = i + 1
        sub_node = node.sub_nodes[i + 1]
        if not sub_node.sub_nodes:
            return sub_node
        while sub_node.sub_nodes:
            sub_node = sub_node.sub_nodes[0]
        return sub_node

    def insert(self, val, sub_node=None):
        if sub_node is None:
            if self.root is None:
                self.root = Node([val])
                return
            sub_node = self.root
            sub_node = self.search_near_node(val, sub_node)
        if len(sub_node.elements) < 3:
            self.element_insert_to_node(val, sub_node)
            return
        else:
            sub_1 = Node([sub_node.elements[0]])
            sub_2 = Node([sub_node.elements[2]])

            if sub_node.parent is None:
                self.root = Node([sub_node.elements[1]], None, [sub_1, sub_2])
                parent_node = self.root
            else:
                parent_node = sub_node.parent
                if len(parent_node.elements) == 3:
                    self.insert(parent_node, sub_node.elements[1])
                else:
                    self.element_insert_to_node(sub_node.elements[1], parent_node)
                for node in parent_node.sub_nodes:
                    if node is sub_node:
                        parent_node.sub_nodes.remove(node)
                        parent_node.sub_nodes.append(sub_1)
                        parent_node.sub_nodes.append(sub_2)

            if val <= sub_node.elements[1]:
                self.element_insert_to_node(val, sub_1)
            else:
                self.element_insert_to_node(val, sub_2)
            sub_1.parent = parent_node
            sub_2.parent = parent_node

    @staticmethod
    def element_insert_to_node(val, tree_node):
        for i in range(len(tree_node.elements)):
            if tree_node.elements[i] > val:
                break
        if tree_node.elements[i] >= val:
            tree_node.elements = tree_node.elements[0:i] + [val] + tree_node.elements[i:len(tree_node.elements)]
        if tree_node.elements[i] < val and i == len(tree_node.elements) - 1:
            tree_node.elements = tree_node.elements[0:i + 1] + [val]

    def element_delete(self, val, node=None):
        if node is None:
            if not self.search_node(val):
                return
            node = self.search_near_node(val)
            successor_node = self.search_successor_node(val, node)
            if node is not successor_node:
                i = 0
                for element in node.elements:
                    if element == val:
                        node.elements[i] = successor_node.elements[0]
                    i = i + 1
                node = successor_node
                val = successor_node.elements[0]
        if len(node.elements) > 1:
            i = 0
            for element in node.elements:
                if element == val:
                    del node.elements[i]
                i = i + 1
        else:
            i = 0
            parent_node = node.parent
            for sub_node in parent_node.sub_nodes:
                if sub_node is node:
                    break
                i = i + 1
            if i < len(parent_node.sub_nodes) - 1:
                element = parent_node.elements[i]
                del parent_node.elements[i]
                self.insert(element, parent_node.sub_nodes[i + 1])
            else:
                element = parent_node.elements[i - 1]
                del parent_node.elements[i - 1]
                self.insert(element, parent_node.sub_nodes[i - 1])
            del parent_node.sub_nodes[i]

if __name__ == '__main__':
    tree = Tree()
    tree.insert(1)
    tree.insert(20)
    tree.insert(3)
    tree.insert(10)
    tree.insert(5)
    tree.insert(34)
    tree.insert(7)
    tree.insert(8)

    tree.element_delete(8)

    tree.insert(8)

    print tree



