# -*- coding: utf-8 -*-

#AVL_tree (Adelson-Velskii and Landis 阿德尔森-维尔斯和兰迪斯) 自平衡树


class ShowNode:
    def __init__(self, row_num, column_num, val):
        self.row_num = row_num
        self.column_num = column_num
        self.val = val


class Node:
    def __init__(self, p_node, l_node, r_node, l_height, r_height, val, type):
        self.p_node = p_node
        self.l_node = l_node
        self.r_node = r_node
        # 左子树高度
        self.l_height = l_height
        # 右子树高度
        self.r_height = r_height
        self.val = val
        # 0 左结点 右结点
        self.type = type


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        node = Node(None, None, None, 0, 0, val, None)
        if self.root is None:
            self.root = node
        else:
            tree_node = self.root
            temp_node = None
            while tree_node is not None:
                if tree_node.val > val:
                    temp_node = tree_node
                    tree_node = tree_node.l_node
                else:
                    temp_node = tree_node
                    tree_node = tree_node.r_node
            node.p_node = temp_node
            if temp_node.val > val:
                node.type = 0
                temp_node.l_node = node
            else:
                node.type = 1
                temp_node.r_node = node
        self.__balance_tree(node, 1)

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
            tree_node.r_node = None
        else:
            tree_node.r_height = self.__max_height(r_node.l_node) + 1
            tree_node.r_node = r_node.l_node
            tree_node.r_node.type = 1
            tree_node.r_node.p_node = tree_node
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
            tree_node.l_node = None
        else:
            tree_node.l_height = self.__max_height(l_node.r_node) + 1
            tree_node.l_node = l_node.r_node
            tree_node.l_node.type = 0
            tree_node.l_node.p_node = tree_node
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
        # 左子树高 > 右子树，差为 2
        if tree_node.l_height - tree_node.r_height == 2:
            self.__right_rotate(tree_node)
            return 0
        # 左子树高 < 右子树，差为 2
        elif tree_node.l_height - tree_node.r_height == -2:
            self.__left_rotate(tree_node)
            return 0
        if tree_node.type == 0:
            # 左结点的右子树 > 左结点的左子树，差为 1
            if tree_node.l_height - tree_node.r_height == -1:
                self.__left_rotate(tree_node)
                return 1
            if tree_node.l_height - tree_node.r_height == 1:
                return 1
        if tree_node.type == 1:
            if tree_node.l_height - tree_node.r_height == -1:
                return 1
            # 右结点的左子树 > 右结点的右子树，差为 1
            if tree_node.l_height - tree_node.r_height == 1:
                self.__right_rotate(tree_node)
                return 1
        return 0

    def remove(self, val):
        key_node = self.search(val)
        if key_node is None:
            raise Exception('node is not exist')

        if self.root == key_node:
            self.root = None

        p_node = key_node.p_node
        l_node = key_node.l_node
        node = self.get_last_left_node(key_node.r_node)
        if node is None:
            l_node.p_node = p_node
            if key_node.type == 0:
                p_node.l_node = l_node
            elif key_node.type == 1:
                p_node.r_node = l_node
            else:
                self.root = l_node
        else:
            key_node.p_node = node.p_node
            node.p_node = p_node
            node.l_node = l_node
            node.r_node = key_node.r_node
            node.l_height = key_node.l_height
            node.r_height = key_node.r_height
            if key_node.type == 0:
                p_node.l_node = node
            elif key_node.type == 1:
                p_node.r_node = node
            else:
                self.root = node
            if node.type == 0:
                key_node.p_node.l_node = None
            else:
                key_node.p_node.r_node = None

        self.__balance_tree(key_node, -1)

    def __balance_tree(self, tree_node, val):
        flag = True
        p_node = tree_node.p_node
        while p_node is not None and flag:
            node_type = tree_node.type
            tree_node = p_node
            if node_type == 0:
                tree_node.l_height = tree_node.l_height + val
            else:
                tree_node.r_height = tree_node.r_height + val
            p_node = tree_node.p_node
            if 0 == self.__rotate(tree_node):
                flag = False

    def search(self, val):
        tree_node = self.root
        while tree_node is not None:
            if tree_node.val > val:
                tree_node = tree_node.l_node
            elif tree_node.val < val:
                tree_node = tree_node.r_node
            else:
                return tree_node
        return None

    def get_last_left_node(self, tree_node):
        if tree_node is None:
            return None
        while tree_node.l_node is not None:
            tree_node = tree_node.l_node
        return tree_node

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
    avl_tree.insert(14)
    avl_tree.insert(15)
    avl_tree.insert(16)
    avl_tree.insert(8)
    avl_tree.insert(3)
    avl_tree.insert(14)
    avl_tree.insert(15)
    avl_tree.insert(16)
    avl_tree.insert(17)
    avl_tree.insert(4)
    avl_tree.insert(8)
    avl_tree.insert(3)
    avl_tree.insert(14)
    avl_tree.insert(15)
    avl_tree.insert(16)
    avl_tree.insert(10)
    avl_tree.insert(12)

    avl_tree.remove(8)

    avl_tree.print_tree()




