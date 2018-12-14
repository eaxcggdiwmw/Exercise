#题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
#程序分析：请抓住分子与分母的变化规律。

fib = [1]
j = 1
for i in range(1, 21):
    fib.append(j)
    j += fib[i-1]
num = 0
line = []
for n in range(1, 19):
    x = (fib[n+1]/fib[n])
    line.append(x)
    num += x
print(fib)
print(line)
print(num)

