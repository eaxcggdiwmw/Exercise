# 题目：读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。
# 程序分析：无。

for i in range(0, 7):
    n = int(input("pls input num:"))
    for j in range(0, n):
        print("*", end='')
    print('')
