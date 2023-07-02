import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
def goodjob(p, n): # 현재 노드와 그사람이 받은 칭찬 점수
    global visited
    for node in tree[p]: # 자식 노드들한테 물려줌
        if not visited[node]:
            visited[node] = True
            score[node] += n
            goodjob(node, score[node])

n, m = map(int, input().rstrip().split())
tree = [[] for _ in range(n+1)]
parent = list(map(int, input().rstrip().split()))
visited = [False] * (n+1)
for i in range(1, n):
    tree[parent[i]].append(i+1)
score = [0]*(n+1)
for _ in range(m):
    p, num = map(int, input().rstrip().split())
    score[p] += num

goodjob(1, 0) # 칭찬의 시작은 사장부터

print(*score[1:])