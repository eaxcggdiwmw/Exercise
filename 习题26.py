#题目：利用递归方法求5!。
#程序分析：递归公式：fn=fn_1*4!

def f(x):

    sum = 0
    if x == 0:
        sum = 1
    else:
        sum = x * f(x - 1)
    return sum

print(f(5))
