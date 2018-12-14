# 题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
# 程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。

a = []
for n in range(1, 10):
    i = int(input("输入数字："))
    a.append(i)
print(a)
for j in range(1, 9):
    for k in range(0, j):
        if a[j] < a[k]:
            x = a[j]
            a[j] = a[k]
            a[k] = x
print(a)
n = int(input("输入要插入的数字"))
a.append(n)
for j in range(1, 10):
    for k in range(0, j):
        if a[j] < a[k]:
            x = a[j]
            a[j] = a[k]
            a[k] = x
print(a)
