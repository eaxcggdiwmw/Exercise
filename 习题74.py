# 题目：列表排序及连接。
# 程序分析：排序可使用 sort() 方法，连接可以使用 + 号或 extend() 方法。

N = 4


def input_line(line):
    for i in range(N):
        j = input("pls input:")
        line.append(j)


def sort_line(line):
    line.sort()
    print(line)


def plus_line(lineA, lineB):
    newline = lineA + lineB
    return newline


if __name__ == '__main__':
    line1 = []
    line2 = []
    input_line(line1)
    input_line(line2)
    sort_line(line1)
    sort_line(line2)
    newline1 = plus_line(line1, line2)
    print(newline1)

