# 题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。
# 已抽签决定比赛名单。有人向队员打听比赛的名单。
# a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。


a = 1
b = 2
c = 3
rang = [a, b, c]
for i in rang:
    if (i != a) and (i != c):
        x = i
for j in rang:
    if (j != c) and (j != x):
        z = j
for k in rang:
    if (k != x) and (k != z):
        y = k
groupA = ["a", "b", "c"]
groupB = ["x", "y", "z"]
print(groupA[x-1], "--", groupB[0],)
print(groupA[y-1], "--", groupB[1],)
print(groupA[z-1], "--", groupB[2],)

