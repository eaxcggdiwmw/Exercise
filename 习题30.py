#题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
#程序分析：无。

num = int(input("pls input num:"))
new = []
for i in range(0, 5):
    m = num//(10**(4-i))
    new.append(m)
    num -= m*(10**(4-i))
new.reverse()
print(new)

if (new[0] == new[4]) and(new[1] == new[3]):
    print("true")
else:
    print("false")
