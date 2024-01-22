from collections import deque
n, k = map(int, input().split())
q = deque([i+1 for i in range(n)])
result = []
print('<', end='')
while q:
    q.rotate(-(k-1))
    if len(q) == 1: print(q[0], end='>')
    else: print(q[0], end=', ')
    q.popleft()