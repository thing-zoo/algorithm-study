import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, k = map(int, input().rstrip().split())
    d = [0]
    d.extend(list(map(int, input().strip().split())))
    indegree = [0] * (n+1)
    tree = [[] for _ in range(n+1)]
    ans = 0
    for _ in range(k):
        a, b = map(int, input().rstrip().split())
        tree[a].append(b)
        indegree[b] += 1
    w = int(input())
    
    queue = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append([i, 0])
    starttime = [0] * (n+1)
    endtime = [0] * (n+1)
    while queue:
        build, start = queue.popleft()
        # print('건물', build, '건설 시작가능 시간', start, '현재시간', ans)
        endtime[build] = max(endtime[build], start + d[build])
        # ans = max(ans, start + d[build])
        if build == w:
            # print(ans)
            print(endtime[w])
            break
        for i in tree[build]:
            indegree[i] -= 1
            starttime[i] = max(endtime[build], starttime[i])
            if indegree[i] == 0:
                queue.append([i, starttime[i]])