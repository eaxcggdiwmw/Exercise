# 题目：打印出杨辉三角形（要求打印出10行如下图）。　　
# 程序分析：无。
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1
# 1 6 15 20 15 6 1
# 1 7 21 35 35 21 7 1
# 1 8 28 56 70 56 28 8 1
# 1 9 36 84 126 126 84 36 9 1

a = []
for i in range(0, 10):
    a.append([1])
    for j in range(1, 10):
        if j < i:
            num = a[i-1][j-1] + a[i-1][j]
            a[i].append(num)
        elif i == 0:
            break
        else:
            a[i].append(1)
            break
for n in range(0, 10):
    print(a[n])
