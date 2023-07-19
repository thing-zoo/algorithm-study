import sys, math
input = sys.stdin.readline
n, m = map(int, input().split())
loc = [[]]

parent = [i for i in range(n+1)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

# 위치 입력 받기
for _ in range(n):
    loc.append(list(map(int, input().split())))

# 이미 연결된 우주신들 연결시키기
for _ in range(m):
    a, b = map(int, input().split())
    if find(a) != find(b):
        union(a, b)

edge = []
# 아직 연결되지 않은 우주신과 다른 우주신들까지 거리를 모두 edge에 저장해야됨
for i in range(1, n+1):
    for j in range(1, n+1): # i~j사이의 거리를 저장
        edge.append([math.sqrt((loc[i][0]-loc[j][0])**2 + (loc[i][1]-loc[j][1])**2), i, j])

edge.sort()
ans = 0
for i in range(len(edge)):
    length, a, b = edge[i]
    if find(a) != find(b):
        union(a, b)
        ans += length

print('%.2f' %ans)