import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
q = deque([ i+1 for i in range(n) ])
data = list(map(int, sys.stdin.readline().split()))
ans = 0
for i in range(m):
    front = 0; back = 0
    for j in range(n):
        if q[j] == data[i]:
            break
        front += 1
    for j in range(-1, -n, -1):
        back += 1
        if q[j] == data[i]:
            break

    if front < back: #2번
        q.rotate(-front)
        ans += front
    else: #3번
        q.rotate(back)
        ans += back
    q.popleft()
print(ans)