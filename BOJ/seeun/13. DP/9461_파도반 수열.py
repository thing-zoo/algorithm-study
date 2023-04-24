n = int(input())

d = [0]*101

d[1] = 1
d[2] = 1
d[3] = 1
d[4] = 2
for i in range(5, 101):
    d[i] = d[i-2]+d[i-3]
for _ in range(n):
    num = int(input())
    print(d[num])
