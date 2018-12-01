# -*- coding: utf-8 -*-


def get_dts(file_path):
    txt = open(file_path, "r")
    lines = txt.readlines()
    count = len(lines)
    i = 0
    dts = []
    dt = None
    while i < count:
        line = lines[i]
        if "dt_start" in line:
            start = line.split(" ")[1]
            s_i = int(start.split(",")[0])
            s_e = int(start.split(",")[1].replace("\\n", ""))
            dt = {
                "start": [s_i, s_e],
                "dt": []
            }
        elif "dt_end" in line:
            start = line.split(" ")[1]
            e_i = int(start.split(",")[0])
            e_e = int(start.split(",")[1].replace("\\n", ""))
            dt["end"] = [e_i, e_e]
            dts.append(dt)
        else:
            dt["dt"].append(line.split(" "))
        i = i + 1
    return dts


def mg(dt):
    max_lj = [0, ""]
    row = len(dt["dt"])
    column = len(dt["dt"][0])
    zx(dt["start"], dt["start"], "", 0, row, column, max_lj, dt["dt"], dt["end"])
    return max_lj


def zx(pre, cur, lj, count, row, column, max_lj, dt, end):
    if cur[0] == end[0] and cur[1] == end[1]:
        if max_lj[0] < count:
            max_lj[0] = count
            max_lj[1] = lj
            return

    if cur[0] - 1 >= 0 and (pre[0] != cur[0] - 1 or pre[1] != cur[1]):
        if dt[cur[0]-1][cur[1]] != "1":
            lj = lj + (", [%s, %s]" % (cur[0], cur[1]))
            count = count + 1
            zx(cur, [cur[0]-1, cur[1]], lj, count, row, column, max_lj, dt, end)
    if cur[0] + 1 < row and (pre[0] != cur[0] + 1 or pre[1] != cur[1]):
        if dt[cur[0] + 1][cur[1]] != "1":
            lj = lj + (", [%s, %s]" % (cur[0], cur[1]))
            count = count + 1
            zx(cur, [cur[0] + 1, cur[1]], lj, count, row, column, max_lj, dt, end)
    if cur[1] - 1 >= 0 and (pre[0] != cur[0] or pre[1] != cur[1] - 1):
        if dt[cur[0]][cur[1] - 1] != "1":
            lj = lj + (", [%s, %s]" % (cur[0], cur[1]))
            count = count + 1
            zx(cur, [cur[0], cur[1] - 1], lj, count, row, column, max_lj, dt, end)
    if cur[1] + 1 < column and (pre[0] != cur[0] or pre[1] != cur[1] + 1):
        if dt[cur[0]][cur[1] + 1] != "1":
            lj = lj + (", [%s, %s]" % (cur[0], cur[1]))
            count = count + 1
            zx(cur, [cur[0], cur[1] + 1], lj, count, row, column, max_lj, dt, end)

    return


if __name__ == '__main__':
    dts = get_dts("data.txt")
    for dt in dts:
        max_lj = mg(dt)
        print '走了 %s 步，具体路径是：%s' % (max_lj[0], max_lj[1])

