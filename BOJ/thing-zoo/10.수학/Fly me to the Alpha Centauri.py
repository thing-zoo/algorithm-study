# 거리      : 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, ...
# 작동 횟수 : 1, 2, 3, 3, 4, 4, 5, 5, 5,  6,  6,  6, ...
# 거리가 2, 6, 12,.., n(n+1)일때 작동횟수가 2, 4, 6,..., n*2
for i in range(int(input())):
    x, y = map(int, input().split())
    dist = y - x # 거리
    n = 1
    while n*(n+1) < dist:
        n += 1
    if dist <= n**2:
        print(n*2-1)
    else:
        print(n*2)