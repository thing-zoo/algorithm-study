import sys
input = sys.stdin.readline
n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append([c, a, b])

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

edges.sort()
ans = []
for i in range(m):
    cost, a, b = edges[i]
    if find(a) != find(b):
        union(a, b)
        ans.append(cost)

print(sum(ans)-max(ans))


