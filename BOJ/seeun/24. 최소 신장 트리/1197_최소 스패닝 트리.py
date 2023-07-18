import sys
input = sys.stdin.readline
v, e = map(int, input().split())
edge = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edge.append([c, a, b])

edge.sort()

parent = [i for i in range(v+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y
ans = 0
for i in range(e):
    c, a, b = edge[i]
    if find(a) != find(b):
        union(a, b)
        ans += c
print(ans)