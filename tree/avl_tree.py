# -*- coding: utf-8 -*-

#AVL_tree (Adelson-Velskii and Landis 阿德尔森-维尔斯和兰迪斯) 自平衡树


class ShowNode:
    def __init__(self, row_num, column_num, val):
        self.row_num = row_num
        self.column_num = column_num
        self.val = val


class Node:
    def __init__(self, p_node, l_node, r_node, l_height, r_height, val):
        self.p_node = p_node
        self.l_node = l_node
        self.r_node = r_node
        self.l_height = l_height #左子树高度
        self.r_height = r_height #右子树高度
        self.val = val
        self.type = None #0 左结点 右结点


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        node = Node(None, None, None, 0, 0, val)
        if self.root is None:
            self.root = node
        else:
            self.__insert(self.root, node)

    def __insert(self, tree_node, node):
        if tree_node.val > node.val:
            if tree_node.l_node is None:
                node.type = 0
                node.p_node = tree_node
                tree_node.l_node = node
                tree_node.l_height = 1
                height = self.__rotate(tree_node)
                return height
            else:
                height = self.__insert(tree_node.l_node, node)
                if height == 1:
                    tree_node.l_height = tree_node.l_height + 1
                    height = self.__rotate(tree_node)
                return height
        else:
            if tree_node.r_node is None:
                node.type = 1
                node.p_node = tree_node
                tree_node.r_node = node
                tree_node.r_height = 1
                height = self.__rotate(tree_node)
                return height
            else:
                height = self.__insert(tree_node.r_node, node)
                if height == 1:
                    tree_node.r_height = tree_node.r_height + 1
                    height = self.__rotate(tree_node)
                return height

    def __left_rotate(self, tree_node):
        p_node = tree_node.p_node
        r_node = tree_node.r_node
        if r_node.l_node is None:
            tree_node.r_height = 0
        else:
            tree_node.r_height = self.__max_height(r_node.l_node) + 1
        tree_node.r_node = r_node.l_node
        tree_node.p_node = r_node
        r_node.p_node = p_node
        r_node.l_node = tree_node
        r_node.l_height = self.__max_height(tree_node) + 1
        if p_node is None:
            self.root = r_node
        else:
            if tree_node.type == 0:
                p_node.l_node = r_node
            else:
                p_node.r_node = r_node
        r_node.type = tree_node.type
        tree_node.type = 0

    def __right_rotate(self, tree_node):
        p_node = tree_node.p_node
        l_node = tree_node.l_node
        if l_node.r_node is None:
            tree_node.l_height = 0
        else:
            tree_node.l_height = self.__max_height(l_node.r_node) + 1
        tree_node.l_node = l_node.r_node
        tree_node.p_node = l_node
        l_node.p_node = p_node
        l_node.r_node = tree_node
        l_node.r_height = self.__max_height(tree_node) + 1
        if p_node is None:
            self.root = l_node
        else:
            if tree_node.type == 0:
                p_node.l_node = l_node
            else:
                p_node.r_node = l_node
        l_node.type = tree_node.type
        tree_node.type = 1

    def __max_height(self, tree_node):
        return max(tree_node.l_height, tree_node.r_height)

    def __rotate(self, tree_node):
        if tree_node.l_height - tree_node.r_height == 2:
            self.__right_rotate(tree_node)
            return 0
        elif tree_node.l_height - tree_node.r_height == -2:
            self.__left_rotate(tree_node)
            return 0
        if tree_node.type == 0:
            if tree_node.l_height - tree_node.r_height == -1:
                self.__left_rotate(tree_node)
                return 1
            if tree_node.l_height - tree_node.r_height == 1:
                return 1
        if tree_node.type == 1:
            if tree_node.l_height - tree_node.r_height == -1:
                return 1
            if tree_node.l_height - tree_node.r_height == 1:
                self.__right_rotate(tree_node)
                return 1
        return 0

    def remove(self, val):
        pass

    def search(self, val):
        pass

    def print_tree(self):
        arr = []
        i = 0
        self.__inorder_traversal(arr, i, self.root)
        for show_node in arr:
            print 'row_num:%s, column_num:%s, val:%s' % (show_node.row_num, show_node.column_num, show_node.val)

    def __inorder_traversal(self, arr, i, tree_node):
        if tree_node.l_node is not None:
            i = self.__inorder_traversal(arr, i, tree_node.l_node)
        row_num = max(tree_node.l_height, tree_node.r_height)
        column_num = i
        arr.append(ShowNode(row_num, column_num, tree_node.val))
        i = i + 1
        if tree_node.r_node is not None:
            i = self.__inorder_traversal(arr, i, tree_node.r_node)
        return i


if __name__ == '__main__':
    avl_tree = AVLTree()
    avl_tree.insert(5)
    avl_tree.insert(8)
    avl_tree.insert(3)
    avl_tree.insert(4)
    avl_tree.insert(10)
    avl_tree.insert(12)
    avl_tree.insert(14)
    avl_tree.insert(15)
    avl_tree.insert(16)
    avl_tree.insert(17)

    avl_tree.print_tree()




