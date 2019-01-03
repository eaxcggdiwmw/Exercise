# 题目：求100之内的素数。
# 程序分析：无。

for i in range(1, 1000):
    flag = 1
    for j in range(2, i):
        if i % j == 0:
            flag = 0
    if flag == 1:
        print(i, end=" ")

