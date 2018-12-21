# 题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
# 程序分析：无。

a = []
num = int(input("pls in put num:"))
for i in range(1, num+1):
    a.append(i)
print(a)

i = 0
k = 0
m = 0

while m < num - 1:
    if a[i] != 0:
        k += 1
    if k == 3:
        a[i] = 0
        k = 0
        m += 1
        print(a)
    i += 1
    if i == num:
        i = 0
i = 0
while a[i] == 0:
    i += 1
print(a[i])




