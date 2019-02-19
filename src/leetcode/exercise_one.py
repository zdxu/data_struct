# -*- coding: utf-8 -*-

# 问题:有2N(3<N<40)个木块,并对之编号为1-N,当然,同一编号需要在两个木块中出现.
# 然后将这些木块这样排序,编号为n的木块间需要间隔n个位置.为了便于把问题说清楚，举例说明．
# 例如当N=3时,
# 将得到入下排序 3 1 2 1 3 2,
# 当Ｎ＝４时,
# 输出
# 4    1    3    1    2    4    3    2
# 当N=5时，没有找到可行的排列
# 当Ｎ＝４０时
# 40   38   39   35   33   37   30   36   27   25
# 34   22   20   32   17   31   13   11   29   7
# 28   3    1    26   1    3    24   7    23   11
# 13   21   17   20   22   25   27   30   33   35
# 38   40   39   37   36   34   32   31   29   28
# 26   24   23   21   19   16   18   15   12   4
# 6    14   2    5    4    2    10   6    9    5
# 8    12   16   15   19   18   14   10   9    8

# 请编写程序找出任意输入4<N<40的一种可行排列．


def get(n):

    arr = []
    for i in range(n-1):
        arr.append(i + 1)

    ret = []
    for i in range(2*n):
        if i == 0 or i == n + 1:
            ret.append(n)
        else:
            ret.append(0)

    temp = 1
    index = n - 2
    while 0 < temp < 2*n:

        item = 0
        for i in range(index + 1):
            if arr[index - i] != 0:
                item = arr[index - i]
                break

        flag = False
        if item == 0:
            flag = True
            for m in arr:
                if m != 0:
                    flag = False
                    break
        if flag:
            break

        if index >= 0 and ret[temp] != 0:
            temp = temp + 1
            index = n - 2
        else:
            if temp + item + 1 >= 2*n or ret[temp + item + 1] != 0 or item == 0:
                if index > 0:
                    index = index - 1
                else:
                    temp = temp - 1
                    if temp == 0:
                        break
                    if temp - ret[temp] - 1 >= 0 and ret[temp - ret[temp] - 1] == ret[temp]:
                        index = -1
                    else:
                        arr[ret[temp]-1] = ret[temp]
                        index = ret[temp] - 2
                        ret[temp + ret[temp] + 1] = 0
                        ret[temp] = 0

            else:
                ret[temp] = item
                ret[temp + item + 1] = item
                arr[item - 1] = 0
                temp = temp + 1
                index = n - 2

    if 0 in ret:
        return []
    return ret


if __name__ == '__main__':
    print get(40)
