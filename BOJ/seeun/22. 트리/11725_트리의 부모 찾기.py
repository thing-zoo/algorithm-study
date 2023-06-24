import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().rstrip().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [0] * (n+1)
def dfs(start):
    
        for n in tree[start]:
            if not visited[n]:
                visited[n] = start
                dfs(n)

dfs(1)
print("\n".join(map(str,visited[2:])))