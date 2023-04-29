import sys
input = sys.stdin.readline
n = int(input())
data = []
data.append([0, 0])
for _ in range(n):
    data.append(list(map(int, input().rstrip().split())))

d = [0]*(n+2)
maxmoney = 0
for i in range(1, n+1):
    day, money = data[i]
    # print(maxmoney, d[i])
    maxmoney = max(d[i], maxmoney)
    if i+day<=n+1:
        print("maxmomey:", maxmoney,"di:", d[i], d[i+day], money+maxmoney)
        d[i+day] = max(maxmoney + money, d[i+day])
print(d)
print(max(d))