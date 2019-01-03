# 题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
# 程序分析：无。

a = []
for n in range(0, 9):
    print("请输入第", n + 1, "个数")
    num = int(input())
    a.append(num)
print(a)
for i in range(0, 9):
    for j in range(i+1, 9):
        if a[i] > a[j]:
            x = a[i]
            a[i] = a[j]
            a[j] = x
print(a)
