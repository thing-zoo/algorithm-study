import sys
input = sys.stdin.readline
n = int(input())
edge = []
parent = [i for i in range(n)]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(i, n):
        edge.append([tmp[j], i, j])

edge.sort()
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
for i in range(len(edge)):
    cost, a, b = edge[i]
    if find(a) != find(b):
        union(a, b)
        ans += cost

print(ans)