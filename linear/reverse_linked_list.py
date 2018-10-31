# -*- coding: utf-8 -*-

# 核心点：
# 1、可转换理论子列个数 n // k
# 2、相邻子列关系满足：
#   若都是转换子列，那么子列1的首元素的next地址指向的是子列2的最末元素地址
#   若后者不是转换子列，那么子列1的首元素的next地址指向的是子列2的首元素地址
# 3、在子列转换运算中要考虑有结点不在链上的情况，所以 1 说的是理论上


line = raw_input()
address = line.split(" ")[0]
n = int(line.split(" ")[1])
k = int(line.split(" ")[2])

nodes = {}
for i in range(n):
    line = raw_input()
    line_params = line.split(" ")
    nodes[line_params[0]] = line_params

count = 0
reverse_sub_list = []
while count < n // k and address != "-1":
    sub_list = []
    i = 0
    while address != "-1" and i < k:
        node = nodes.get(address)
        sub_list.insert(0, {"address": address, "val": node[1], "next": node[2]})
        if i == k - 1:
            sub_list[k-1]["next"] = node[2]
        if i > 0:
            sub_list[0]['next'] = sub_list[1]["address"]
        address = node[2]
        i = i + 1

    if i == k:      # 相邻右子列为可转换子列
        if reverse_sub_list:
            reverse_sub_list[k - 1]["next"] = sub_list[0]["address"]
            for item in reverse_sub_list:
                print "%s %s %s" % (item["address"], item["val"], item["next"])
            reverse_sub_list = []
        reverse_sub_list = sub_list
        count = count + 1
    else:           # 有部分结点不在链上
        address = sub_list[len(sub_list) - 1]["address"]
        sub_list = []
        count = n // k

if reverse_sub_list:    # 相邻右子列非可转换子列
    for item in reverse_sub_list:
        print "%s %s %s" % (item["address"], item["val"], item["next"])

while address != "-1":
    node = nodes.get(address)
    print "%s %s %s" % (node[0], node[1], node[2])
    del nodes[address]
    address = node[2]

# line1 = raw_input()
# address = line1.split(" ")[0]
# n = int(line1.split(" ")[1])
# k = int(line1.split(" ")[2])
#
# params_by_next = {}
# params_by_address = {}
# for i in range(n):
#     line = raw_input()
#     line_params = line.split(" ")
#     params_by_address[line_params[0]] = {"val": line_params[1], "next": line_params[2]}
#     params_by_next[line_params[2]] = {"val": line_params[1], "address": line_params[0]}
#
# result = []
# count = 0
# temp_address = None
# while address != "-1" and params_by_address.get(address):
#     item_by_address = params_by_address[address]
#     address = item_by_address["next"]
#     count = count + 1
#     if count % k == 0:
#         temp_address = address
#         temp = address
#         for i in range(k):
#             item_by_next = params_by_next[temp]
#             current_address = item_by_next["address"]
#             if i != k - 1:
#                 next_address = params_by_next[current_address]["address"]
#             else:
#                 next_address = address
#                 if params_by_next.get(current_address):
#                     result[count-k-1]["next"] = params_by_next[address]["address"]
#             result.append({"address": current_address, "val": item_by_next["val"], "next": next_address})
#             # del params_by_next[temp]
#             temp = item_by_next["address"]
#             # del params_by_address[item_by_next["address"]]
#
# if address != "-1":
#     print 0
# else:
#     while temp_address != "-1":
#         item_by_address = params_by_address[temp_address]
#         result.append({"address": temp_address, "val": item_by_address["val"], "next": item_by_address["next"]})
#         temp_address = item_by_address["next"]
#         # del params_by_address[params_by_next[address]["address"]]
#         # del params_by_next[address]
#
#     for item in result:
#         print "%s %s %s" % (item["address"], item["val"], item["next"])


# 00100 8 4
# 00000 4 99999
# 00100 1 12309
# 68237 6 -1
# 33218 3 00000
# 99999 5 68237
# 12309 2 33218
# 71234 7 81234
# 81234 8 -1