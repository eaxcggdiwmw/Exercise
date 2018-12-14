#题目：输入某年某月某日，判断这一天是这一年的第几天？
#程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：

Y = int(input("input year:"))
M = int(input("input month:"))
D = int(input("input day:"))
months = (0,31,59,90,120,151,181,212,243,273,304,334)
if (Y > 0):
    y = Y
    if (Y%4 == 0 and Y%100 != 0):
        f = 1
    else:
        f = 0
else:
    print('input year error')
if (0 < M < 12):
    m = M
else:
    print('input month error')
if (M in(1,3,5,7,8,10,12) and 0 < D < 32 ) or (M in(4,6,9,11) and 0 < D < 31 ) or (M == 2 and f ==1 and 0 < D < 29) or (M == 2 and f ==0 and 0 < D < 30):
    d = D
    totalday = months[m-1] + d
    print (y,"年",m,"月",d,"日是",y,"年的第",totalday,"天")
else:
    print('input day error')

