from collections import deque
a, b = map(int, input().split())

def bfs(a, b):
    queue = deque()
    queue.append([a, 0])
    while queue:
        x, cnt = queue.popleft()
        if x > b:
            continue
        if x == b: # b가 만들어지면 종료
            return cnt
        queue.append([x*2, cnt+1]) # *2
        queue.append([x*10+1, cnt+1]) # 뒷자리에 1더하기
    return False

ans = bfs(a, b)
if not ans:
    print(-1)
else:
    print(ans+1)