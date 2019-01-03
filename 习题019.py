#题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
#程序分析：请参照程序Python 练习实例14。

for i in range(2, 1001):
    num = i
    a = []
    m = 0
    for j in range(1, i):
        if num % j == 0:
            a.append(j)
    for n in a:
        m += n
    if m == i:
        print(m, a)

