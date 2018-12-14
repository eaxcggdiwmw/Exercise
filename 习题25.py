# 题目：求1+2!+3!+...+20!的和。
# 程序分析：此程序只是把累加变成了累乘。

a = []
total = 0
for i in range(1, 22):
    num = 1
    a = []
    for j in range(1, i):
        num *= j
        a.append(num)
for n in a:
    total += n
print(a)
print(total)
