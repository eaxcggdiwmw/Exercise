# 题目：打印出如下图案（菱形）:

#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

# 程序分析：先把图形分成两部分来看待，前四行一个规律，后三行一个规律，利用双重for循环，第一层控制行，第二层控制列。

for i in range(0, 5):
    for n in range(0, 4-i):
        print(" ", end=" ")
    for m in range(0, (i-1)*2+1):
        print("*", end=" ")
    print("")
for j in range(1, 4):
    for x in range(0, j):
        print(" ", end=" ")
    for y in range(0, 7-(j*2)):
        print("*", end=" ")
    print("")

