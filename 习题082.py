# 题目：八进制转换为十进制
# 程序分析：无。

num = int(input("pls input num:"))

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
print(num)
print(new)
newnum = 0
new.reverse()
print(new)
for a in range(0, x):
    newnum += (new[a]*(8**a))
    print(new[a])
    print(new[a]*(8**a))
    print(newnum)
print(newnum)

