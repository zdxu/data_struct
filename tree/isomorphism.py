# -*- coding: utf-8 -*-


class Node:

    def __init__(self, right, left, val):
        self.right = right
        self.left = left
        self.val = val


def eq(node1, node2):
    if node1 is not None and node2 is not None:
        if node2.val == node1.val:
            return True
    return node1 == node2


def judge_isomorphism(t1, t2):
    if eq(t1, t2):
        if t1 is None:
            return True
        else:
            if judge_isomorphism(t1.right, t2.right) and judge_isomorphism(t1.left, t2.left):
                return True
            if judge_isomorphism(t1.right, t2.left) and judge_isomorphism(t1.left, t2.right):
                return True
            return False
    else:
        return False


def init_tree(level, flag):
    arr = None
    root = None
    for i in range(level):
        if i == 0:
            root = Node(None, None, '%d' % 1)
            arr = [root]
        else:
            temp = []
            for j in range(len(arr)):
                if flag:
                    arr[j].left = Node(None, None, 'r%d%d' % (i+1, j))
                    arr[j].right = Node(None, None, 'l%d%d' % (i+1, j))
                    temp.append(arr[j].right)
                    temp.append(arr[j].left)
                else:
                    arr[j].left = Node(None, None, 'l%d%d' % (i+1, j))
                    arr[j].right = Node(None, None, 'r%d%d' % (i+1, j))
                    temp.append(arr[j].left)
                    temp.append(arr[j].right)
            arr = temp
    return root


if __name__ == '__main__':
    t1 = init_tree(5, False)
    t2 = init_tree(5, True)
    print judge_isomorphism(t1, t2)
