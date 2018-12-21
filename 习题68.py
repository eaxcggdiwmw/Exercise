# 题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
# 程序分析：无。

a = []
n = int(input("pls in put n:"))
for i in range(0, n):
    x = input("pls input num:")
    a.append(x)
print(a)

m = int(input("pls in put m:"))
for j in range(0, m):
    num = a.pop(n-1)
    a.insert(0, num)
print(a)
