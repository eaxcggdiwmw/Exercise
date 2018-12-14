#题目：将一个列表的数据复制到另一个列表中。
#程序分析：使用列表[:]。

n = int(input("输入数字数量:"))
a = []
for i in range(0,n):
    print("输入第",i+1,"个数字:")
    a.append(input())
b = a[:]
print (b)