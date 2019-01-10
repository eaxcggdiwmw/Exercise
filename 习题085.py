# 题目：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。
# 程序分析：999999 / 13 = 76923。

x = int(input("pls input num:"))
num = 9
n = 1
while num % x != 0:
    num = (num*10+9)
    n += 1
print("需要", n, "个 9")
print(num)
