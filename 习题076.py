# 题目：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
# 程序分析：无。


def func(a):
    if (a % 2) == 0:
        func1(a)
    else:
        func2(a)


def func1(b):
    j = 0
    for i in range(1, b):
        if (b - i) % 2 == 0:
            j += 1/i
            print(j)
    print(j)


def func2(c):
    m = 0
    for n in range(1, c):
        if (c - n) % 2 == 0:
            m += 1/n
            print(m)
    print(m)


if __name__ == '__main__':
    num = int(input("pls input num:"))
    func(num)
