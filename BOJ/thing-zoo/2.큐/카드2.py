from collections import deque

n = int(input())
q = deque()
for i in range(n):
    q.append(i+1)

while len(q) > 1:
    # front 버리기
    if len(q) > 1:
        q.popleft()
    # 다음 front를 맨 뒤로
    if len(q) > 1:
        q.append(q.popleft())
print(q.popleft())