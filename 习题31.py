# 题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
# 程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。。

week = input("pls input week:")
if week[0] == "M":
    print("Monday")
elif week[0] == "F":
    print("Friday")
elif week[0] == "W":
    print("Wensday")
elif week[0] == "S":
    if week[1] == "t":
        print("Statday")
    elif week[1] == "u":
        print("Sunday")
elif week[0] == "T":
    if week[1] == "u":
        print("Tuesday")
    elif week[1] == "r":
        print("Trisday")