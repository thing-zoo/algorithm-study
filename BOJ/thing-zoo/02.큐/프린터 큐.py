from collections import deque
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    temp = list(map(int, input().split()))
    priority = deque([(i, temp[i]) for i in range(n)])
    order = 0
    while priority:
        idx, pri = priority.popleft()
        if priority:
            temp = [priority[i][1] for i in range(len(priority))]
            if pri < max(temp):
                priority.append((idx, pri))
                continue
        order += 1
        if idx == m:
            print(order)
            break