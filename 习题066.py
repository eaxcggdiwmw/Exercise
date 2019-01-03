# 题目：输入3个数a,b,c，按大小顺序输出。　　　
# 程序分析：无。

a = int(input("请输入a："))
b = int(input("请输入b："))
c = int(input("请输入c:"))
linea = []

if a > b:
    if b > c:
        linea.append(a)
        linea.append(b)
        linea.append(c)
    else:
        if a > c:
            linea.append(a)
            linea.append(c)
            linea.append(b)
        else:
            linea.append(c)
            linea.append(a)
            linea.append(b)
else:
    if a > c:
        linea.append(b)
        linea.append(a)
        linea.append(c)
    else:
        if b > c:
            linea.append(b)
            linea.append(c)
            linea.append(a)
        else:
            linea.append(c)
            linea.append(b)
            linea.append(a)
print(linea)
