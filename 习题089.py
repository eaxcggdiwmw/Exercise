# 题目：某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：
# 每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
# 程序分析：无。

num1 = []
for i in range(0, 4):
    n = int(input("pls input num:"))
    num1.append(n)
print(num1)


def code(num):
    for x in range(0, 4):
        num[x] = (num[x] + 5) % 10
    m = num[0]
    num[0] = num[3]
    num[3] = m
    n = num[1]
    num[1] = num[2]
    num[2] = n
    print(num)
    return num


new = code(num1)

