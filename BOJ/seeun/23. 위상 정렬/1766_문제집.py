import sys, heapq
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
tree = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
for _ in range(m):
    before, after = map(int, input().rstrip().split())
    indegree[after] += 1
    tree[before].append(after)

queue = []
for i in range(1, n+1):
    tree[i].sort()
    if indegree[i] == 0:
        heapq.heappush(queue,i) # 쉬운 문제부터 풀어야하므로 힙으로 관리

while queue:
    prob = heapq.heappop(queue) # 풀수 있는 문제들 중에서 가장 난이도가 작은 문제가져오기
    print(prob, end=" ")
    for i in tree[prob]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(queue,i)