import sys
input = sys.stdin.readline

n = int(input())
wine = []
for _ in range(n):
    wine.append(int(input()))

d = [[0]*3 for _ in range(n)]

drink = -1
# i = i번째 와인을 마심, J = 연속해서 j번째
if n == 1:
    print(wine[0])
else:
    d[0][0] = wine[0]
    d[0][1] = wine[0]
    d[0][2] = 0
    for i in range(1, n):
        d[i][0] = d[i-1][2] + wine[i]
        d[i][1] = d[i-1][0] + wine[i] #
        d[i][2] = max(d[i-1]) # 
    # print(d)
    print(max(d[n-1]))