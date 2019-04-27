# -*- coding: utf-8 -*-

# 一种含有红黑结点并能够自平衡的二叉树，满足以下性质：
# 性质一：每个结点要么是黑色要么是红色
# 性质二：根结点是黑色
# 性质三：每个叶子结点是黑色（叶子结点是 null 结点，不包含数据只是充当树在此结束的指示）
# 性质四：每个红色结点的两个子结点一定是黑色结点
# 性质五：任意结点到每个叶子结点的路径都包含相同数量的黑结点

# ----  当前结点为黑色或空树时  ----
# 当前结点是根结点或者树为空树 直接插
# 当前结点是黑色 插入结点置为红色即可（原先一定是红黑树，满足性质五，置为红色后任然满足性质五）

# 左倾
# ----  当前结点为红色，则父结点也必是黑色  ----
#       1、无同级结点(当前结点为树尾结点)，先插入后转换
#           黑                            黑（原当前）
#       红（当前）        ->          红        红（原黑）
#   红

#           黑                            黑
#       红（当前）        ->          红（原当前）红（原黑）
#           红

#
#       2、有同级结点，先转换后插入
#       a、同级结点为红色，
#       步骤-：
#               黑                            红（原黑）                               红（原黑）
#           红（当前）红      ->           黑（当前）黑（同级）         ->            黑（当前）黑（同级）
#       红                                                                     红

#               黑                            红（原黑）                               红（原黑）
#           红（当前）红      ->           黑（当前）黑（同级）           ->          黑（插入）黑（同级）
#               红                            红                               红（当前）
#      步骤二：已父结点为当前结点，插入已祖父结点为树末结点的树即作为祖父结点的子结点，循环利用1、2的方法，不同之处是在祖父结点的插入
# 可能会遇到
#            黑
#       红       黑       这种情况同方法1


# 删除最终都转换成了，树尾结点替换并删除树尾结点

# 步骤-：查找树尾替换结点

# 替换结点为红色 直接删

# 替换结点为黑色
# 黑 红 黑
#    1 叔结点有少于两个子结点 以父结点为当前结点旋转，树尾结点置红
#    2 叔结点有两个子结点 以父结点为当前结点旋转，树尾结点置红 + 新插入叔结点的一个子结点
# 黑 黑 红
#


class Node:
    def __init__(self, val):
        self.val = val
        self.color = 0                  # 0 红 1 黑
        self.left_node = None
        self.right_node = None
        self.parent = None


class Tree:
    def __init__(self):
        self.root = None

    def search(self, val):
        sub_node = self.root
        while sub_node:
            if sub_node.val == val:
                return sub_node
            if sub_node.val < val:
                sub_node = sub_node.left_node
            if sub_node.val > val:
                sub_node = sub_node.right_node
        return None

    @staticmethod
    def search_successor_node(node):
        ret = node
        sub_node = node.left_node
        while sub_node:
            ret = sub_node
            if sub_node.right_node:
                sub_node = sub_node.right_node
        return ret

    @staticmethod
    def search_near_node(root, val):
        ret = root
        sub_node = root
        while sub_node:
            ret = sub_node
            if sub_node.val <= val:
                sub_node = sub_node.right_node
            else:
                sub_node = sub_node.left_node
        return ret

    def insert_node(self, in_node, node=None):
        if not node:
            if self.root is None:
                in_node.color = 1
                self.root = in_node
                return
            node = Tree.search_near_node(self.root, in_node.val)
        if node.color == 1:
            Tree.combination_node(node, in_node)
            if self.root.parent:
                in_node.color = 1
                in_node.parent = None
                self.root = in_node
        else:
            parent = node.parent
            if parent.left_node is None or parent.right_node is None\
                    or parent.left_node.color == 1 or parent.right_node.color == 1:
                Tree.combination_node(node, in_node)
                if parent.left_node:
                    current_node = parent.left_node
                else:
                    current_node = parent.right_node
                if parent.parent:
                    current_node.parent = parent.parent
                    if parent.parent.left_node == parent:
                        parent.parent.left_node = parent.left_node
                    else:
                        parent.parent.right_node = parent.right_node
                else:
                    self.root = current_node
                current_node.right_node = parent
                parent.color = 0
                parent.left_node = None
            else:
                parent.left_node.color = 1
                parent.right_node.color = 1
                Tree.combination_node(node, in_node)
                if parent.parent:
                    self.insert_node(parent, parent.parent)

    @staticmethod
    def combination_node(node, in_node):
        if node.val >= in_node.val:
            in_node.parent = node
            in_node.color = 0
            node.left_node = in_node
        elif node.left_node and node.left_node.color == 0:
            in_node.parent = node
            in_node.color = 0
            node.right_node = in_node
        else:
            if node.parent:
                in_node.parent = node.parent
                if node.parent.left_node == node:
                    node.parent.left_node = in_node
                else:
                    node.parent.right_node = in_node
            in_node.parent = node.parent
            node.parent = in_node
            node.color = 0
            node.right_node = in_node.left_node
            in_node.color = 1
            in_node.left_node = node

    def delete(self, val):
        node = self.search(val)
        if not node:
            return
        parent = node.parent
        if not parent:
            self.root = None
            return
        successor_node = Tree.search_successor_node(node)
        if successor_node == node:
            if not parent:
                self.root = node.left_node
                node.left_node.parent = None
            else:
                if parent.left_node == successor_node:
                    parent.left_node = node.left_node
                else:
                    parent.right_node = node.left_node
                node.left_node = parent
            return
        node.val = successor_node.val
        if successor_node.color == 0:
            parent = successor_node.parent
            if parent.left_node == successor_node:
                parent.left_node = None
            else:
                parent.right_node = None
            return



if __name__ == '__main__':
    tree = Tree()
    tree.insert_node(Node(1))
    tree.insert_node(Node(2))
    tree.insert_node(Node(3))
    tree.insert_node(Node(4))
    tree.insert_node(Node(5))
    tree.insert_node(Node(6))
    tree.insert_node(Node(7))
    tree.insert_node(Node(8))

    print tree
