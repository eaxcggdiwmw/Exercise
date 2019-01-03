# 题目：求输入数字的平方，如果平方运算后小于 50 则退出。
# 程序分析：无
flag = 1
while flag == 1:
    print("pls input num:")
    num = int(input())
    numplus = num * num
    print(numplus)
    if numplus < 50:
        flag = 0
