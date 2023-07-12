import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n = int(input())
m = int(input())
tree = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
basic = []
for _ in range(m):
    x, y, k = map(int, input().rstrip().split())
    tree[y].append((x, k)) # x를 만들려면 y k개가 필요함
    indegree[x] += 1

queue = deque()
for i in range(1, n+1):
    if indegree[i] == 0: # 기본 부품인 경우에 큐, basic에 넣어줌
        queue.append(i)
        basic.append(i)

need = [[0]*(n+1) for _ in range(n+1)] # i를 만들기위해 j가 [i][j]개 필요함
while queue:
    res = queue.popleft()
    for i, num in tree[res]: # res를 필요로 하는 부품들, i를 만들기위해서 num개가 필요함
        if res in basic: # res가 기본부품이라면
            need[i][res] += num # i를 만들기 위해서는 res가 num개 필요함
        else: # res가 중간부품이라면 res를 만들 기본 부품이 필요함
            for j in range(1, n+1): # 
                need[i][j] += need[res][j]*num # i를 만들기 위한 기본부품 j: res를 만들기위한 기본부품j*num
        indegree[i]-= 1
        if indegree[i] == 0:
            queue.append(i)
for i in range(1, n+1):
    if need[n][i] >0:
        print(i, need[n][i])
