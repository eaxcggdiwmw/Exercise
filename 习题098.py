# 题目：从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。
# 程序分析：无。

from sys import stdout


def switch(strings):
    strings = strings.upper()
    return strings


filename = input('输入文件名:\n')
fp = open(filename, "w")
ch = input('输入字符串:\n')
ch = switch(ch)
fp.write(ch)
stdout.write(ch)
fp.close()


