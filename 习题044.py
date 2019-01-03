# 两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：
# 程序分析：创建一个新的 3 行 3 列的矩阵，使用 for 迭代并取出 X 和 Y 矩阵中对应位置的值，相加后放到新矩阵的对应位置中。
import time
a = []
b = []
c = []

for i in range(0, 3):
    a.append([])
    for j in range(0, 3):
        x = int(input("pls input num in a:"))
        a[i].append(x)
print(a)
for i in range(0, 3):
    b.append([])
    for j in range(0, 3):
        y = int(input("pls input num in b:"))
        b[i].append(y)
print(b)
time.sleep(3)
for i in range(0, 3):
    c.append([])
    for j in range(0, 3):
        z = a[i][j] + b[i][j]
        c[i].append(z)
print(c)