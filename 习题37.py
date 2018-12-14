# 题目：对10个数进行排序。
# 程序分析：可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。
a = []
for n in range(1, 10):
    i = int(input("输入数字"))
    a.append(i)
print(a)
for j in range(1, 9):
    for k in range(0, j):
        if a[j] < a[k]:
            x = a[j]
            a[j] = a[k]
            a[k] = x
print(a)
