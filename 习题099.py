# 题目：有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
# 程序分析：无。


from sys import stdout

filename1 = input('输入文件名:\n')
fp1 = open(filename1)
a = fp1.read()
fp1.close()
filename2 = input('输入文件名:\n')
fp2 = open(filename2)
b = fp2.read()
fp2.close()
filename3 = input('输入文件名:\n')
fp3 = open(filename3, "w")
fp3.write(a + b)
stdout.write(a + b)
fp3.close()
