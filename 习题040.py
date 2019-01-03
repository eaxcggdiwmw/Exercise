# 题目：将一个数组逆序输出。
# 程序分析：用第一个与最后一个交换。
a = []
for n in range(1, 10):
    i = int(input("输入数字："))
    a.append(i)
print(a)
for j in range(1, 9):
    for k in range(0, j):
            x = a[j]
            a[j] = a[k]
            a[k] = x
print(a)

