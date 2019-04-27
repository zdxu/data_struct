# -*- coding: utf-8 -*-

# Dijkstra(迪杰斯特拉)算法
# 核心
#   每次已新扩散结点群的最短路径为新的遍历起始点
#   去除起始点到该结点非最短路径的路径选择
#   示例:
#      A 为起始结点， B 结点相邻结点 C、D
#      若 A->B 、A->E->B、A->F->B 中 A->F->B 是A 至 B 最短距离的路径，
#   那么 A->F->B->D、A->F->B->C 也必是上述三条可选路径中最短的路径


# 结点名: {"way": "A->B", "distance": 10}
ret = {}
temp_queue = []


def dijkstra(graph, start_node_name):
    """
    迪杰斯特拉算法获取起始结点到其它结点的最短距离路经
    :param graph: 有权图
    :param start_node_name: 起始结点名称
    :return: 返回列表 所有结点（结点名称，从该起始点到各其它结点的最短距离，具体路径）
    """

    ret[start_node_name] = {"way": start_node_name, "distance": 0}
    temp_min_distance = 0
    temp_queue.append({"name": start_node_name, "way": start_node_name, "distance": 0})
    queue_len = len(temp_queue)
    num = 0

    for item_node in temp_queue:
        num = num + 1
        arr = graph[item_node["name"]]
        for item in arr:
            way = item_node["way"] + "->" + item["name"]
            distance = item_node["distance"] + item["distance"]

            # 通过该路径到达该结点非最短路径，那么由该点中转到相邻结点也不会是到起始点到该结点相邻点的最短路径
            if item["name"] in ret and ret[item["name"]]["distance"] <= distance:
                continue

            if item["name"] not in ret:
                # 到达结点之前未到达过
                ret[item["name"]] = {"way": way, "distance": distance}
            elif ret[item["name"]]["distance"] > distance:
                # 到达结点之前已有其它路径经过，且本次到达的路径距离比之前要短
                ret[item["name"]]["way"] = way
                ret[item["name"]]["distance"] = distance

            # 获取本次扩散的最短距离
            if temp_min_distance > distance:
                temp_min_distance = distance
                # 将最短距离的扩散结点存放在本次新增扩散队列的首部
                temp_queue.insert(queue_len - 1, {"name": item["name"], "way": way, "distance": distance})
            else:
                temp_queue.append({"name": item["name"], "way": way, "distance": distance})
        # 开启新的扩散队列的扩散
        if num >= queue_len:
            queue_len = len(temp_queue)

init_graph = {
    "A": [
        {"name": "B", "distance": 12},
        {"name": "F", "distance": 16},
        {"name": "G", "distance": 14}
    ],
    "B": [
        {"name": "A", "distance": 12},
        {"name": "C", "distance": 10},
        {"name": "F", "distance": 7}
    ],
    "C": [
        {"name": "B", "distance": 10},
        {"name": "F", "distance": 6},
        {"name": "E", "distance": 5},
        {"name": "D", "distance": 3}
    ],
    "D": [
        {"name": "C", "distance": 3},
        {"name": "E", "distance": 4}
    ],
    "E": [
        {"name": "D", "distance": 3},
        {"name": "F", "distance": 2},
        {"name": "C", "distance": 5},
        {"name": "G", "distance": 8}
    ],
    "F": [
        {"name": "B", "distance": 7},
        {"name": "C", "distance": 6},
        {"name": "E", "distance": 2},
        {"name": "G", "distance": 9},
        {"name": "A", "distance": 16}
    ],
    "G": [
        {"name": "A", "distance": 14},
        {"name": "F", "distance": 9},
        {"name": "E", "distance": 8}
    ]
}

dijkstra(init_graph, "D")

print ret





