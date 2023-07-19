import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
power = list(map(int, input().split()))
edge = []
parent = [i for i in range(n+1)]
for p in power:
    edge.append([0, 0, p]) # 발전소를 가지고 있음: 0->p로 표현
    parent[p] = 0 # 따라서 부모는 0으로 설정, union-find를 할 때 작은 노드를 부모로 가짐을 이용
    
for _ in range(m):
    a, b, c = map(int, input().split())
    edge.append([c, a, b])

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

ans = 0
for i in range(len(edge)):
    c, a, b = edge[i]
    if find(a) != find(b):
        union(a, b)
        ans += c
print(ans)