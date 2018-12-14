#题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
#程序分析：关键是计算出每一项的值。

a = int(input("pls input num"))
n = int(input("pls input how many times"))
j = n - 1
num = 0
total = 0
for i in range(0, j + 1):
    m = j - i
    while m >= 0:
        x = a*(10**m)
        num += x
        m -= 1
    if i == j:
        print(num, end='=')
    else:
        print(num, end='+')
    total += num
    num = 0
print(total)
