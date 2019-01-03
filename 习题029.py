# 题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
# 程序分析：学会分解出每一位数。

num = int(input("pls input num"))
x = 0
new = []
for n in range(1, 100):
    if num < 10:
        print(num, "是", 1, "位数")
        break
    elif (num % (10**n) == num) and (num >= 10):
        x = n
        print(num, "是", x, "位数")
        break
for i in range(0, x):
    m = num//(10**(x-i-1))
    new.append(m)
    num -= m*(10**(x-i-1))
new.reverse()
print(new)
