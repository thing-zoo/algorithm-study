import sys
input = sys.stdin.readline
n, m = map(int, input().split())
edge = []
a, b, start = map(int, input().split()) # 입구에서 1번까지의 정보는 따로 저장

for _ in range(m):
    a, b, c = map(int, input().split())
    edge.append([c, a, b])

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

# 최악의 경우 탐색
up = 0
if start == 0:
    up += 1
edge.sort() # 오르막을 기준으로 
parent = [i for i in range(n+1)]
for i in range(m):
    c, a, b = edge[i]
    if find(a) != find(b):
        union(a, b)
        if c == 0:
            up += 1
bad = up * up

# 최적의 경우 탐색
up = 0
if start == 0:
    up += 1
edge.sort(reverse=True) # 내리막 먼저
parent = [i for i in range(n+1)]
for i in range(m):
    c, a, b = edge[i]
    if find(a) != find(b):
        union(a, b)
        if c == 0:
            up += 1
good = up * up

print(bad-good)