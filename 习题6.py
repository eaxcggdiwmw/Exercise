#题目：斐波那契数列。
#程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
#在数学上，费波那契数列是以递归的方法来定义：

a = int(input("需要输出的个数："))
def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1,1]
    else:
        fibs = [1,1]
        for i in range(1,n):
            fibs.append(fibs[i] + fibs[i-1])
        return fibs
print (fib(a))