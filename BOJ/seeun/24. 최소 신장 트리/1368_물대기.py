import sys
input = sys.stdin.readline

n = int(input())
dig = []
edge = []
parent = [i for i in range(n+1)]
for i in range(1, n+1):
    edge.append([int(input()), 0, i])

for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    for j in range(1, n+1):
        edge.append([tmp[j-1], i, j])

edge.sort()

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

ans =0
for i in range(len(edge)):
    cost, a, b = edge[i]
    if find(a) != find(b):
        union(a, b)
        ans += cost

print(ans)