import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n+1)]
times = [0] * (n+1)
indegree = [0] * (n+1)
for i in range(1, n+1):
    info = list(map(int, input().rstrip().split()))
    times[i] = info[0]
    if info[1] > 0:
        for j in range(2, 2+info[1]):
            tree[info[j]].append(i)
            indegree[i] += 1

queue = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append([i, 0])
    
time = 0 # 현재 시간
start = [0] * (n+1) # 시작할 수 있는 시간
while queue:
    work,now = queue.popleft()
    if now+times[work] > time: # 작업시작 가능 시간 + 작업시간 > 현재 시간
        time = now+times[work]
    for i in tree[work]: # 후수 작업들
        indegree[i] -= 1
        start[i] = max(now + times[work], start[i]) # i작업이 시작할 수 있는 시간을 갱신해줌(여러개가 있다면 제일 마지막에 끝나는 것 기준으로 시작할 수 있음)
        if indegree[i] == 0: # 선수 작업이 다 끝났다면
            queue.append([i, start[i]]) # 작업 시작할 수 있음

print(time)