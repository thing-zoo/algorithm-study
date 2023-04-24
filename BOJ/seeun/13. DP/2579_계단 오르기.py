n = int(input())
stairs = []
stairs.append(0)
for _ in range(n):
    stairs.append(int(input()))

d = [[0]*3 for _ in range(n+1)]

if n == 1:
    print(stairs[1])
else:
    d[1][1] = stairs[1]
    d[2][1] = stairs[2]
    d[2][2] = stairs[1] + stairs[2]
    for i in range(3, n+1):
        d[i][1] = max(d[i-2][1], d[i-2][2])+stairs[i] 
        d[i][2] = d[i-1][1] + stairs[i] # 무조건 한칸전에서 옴
    print(max(d[n][1], d[n][2]))