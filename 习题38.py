# 题目：求一个3*3矩阵主对角线元素之和。
# 程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。
a = []
for i in range(0, 3):
    a.append([])
    for j in range(0, 3):
        x = int(input("pls input num:"))
        a[i].append(x)
num = 0
for m in range(0,3):
    for n in range(0,3):
        if m == n:
            print(a[m][n])
            num += a[m][n]
print(num)


