from collections import deque

n = int(input())
deq = deque([i+1 for i in range(n)])

check = True

while len(deq) != 1:
    if check ==  True:
        deq.popleft()
        check = False
    else:
        deq.append(deq.popleft())
        check = True

print(*deq)