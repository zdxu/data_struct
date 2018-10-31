# -*- coding: utf-8 -*-
# 核心点：
# 1、出栈的数一定大于等于栈内的数或者大于已出栈最大数
# 2、若出栈的数大于已出栈最大数，则栈内一定存在出栈数与已出栈最大数区间的数字
# 3、若出栈的数小与已出栈最大数，则该将要出栈的数一定在栈内且即是栈顶的那个数
#
#

line1 = raw_input()

M = int(line1.split(" ")[0])
N = int(line1.split(" ")[1])
K = int(line1.split(" ")[2])
data = []
for i in range(K):
    data.append(raw_input().split(" "))

result = []
for arr in data:
    flag = True
    # 已使用栈内存储的数列，下标大的代表越靠前入栈
    use_stack = []
    # 已出栈的最大数，默认为 0
    temp = 0
    for i in range(len(arr)):
        val = int(arr[i])
        if temp == val:     # 已出栈的最大数再次出现
            flag = False
            break
        elif temp < val:    # 当前出栈的数大于已出栈的最大数
            for j in range(val-temp-1):     # 将区间部分的数入栈，不包括 val
                use_stack.append(temp+j+1)  # 值大的后入栈
            if M <= len(use_stack):         # 已使用栈空间超过了栈的设定空间，这里有等于是因为已使用栈存储的是差值部分的数据
                flag = False
                break
            temp = val      # 更新已出栈最大数
        else:               # 当前出栈数小于已出栈的最大数
            if val != use_stack[len(use_stack)-1]:      # 将要从已使用栈出栈的数要等于 val
                flag = False
                break
            del use_stack[len(use_stack)-1]             # 出栈
    if flag:
        result.append("YES")
    else:
        result.append("NO")


for flag in result:
    print flag


# 5 7 5
