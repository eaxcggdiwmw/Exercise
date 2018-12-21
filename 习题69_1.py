# 题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
# 程序分析：无。

a = []
num = int(input("pls in put num:"))
for i in range(1, num+1):
    a.append(i)
print(a)

n = 0
m = 0
j = 0
k = 0
while len(a) != 1:
    if j == 3:
        del a[n-1]
        j = 1
        print(a)
    if n >= len(a):
        n = 0
    j += 1
    n += 1
