import sys 
from collections import deque
n = int(input())

queue = deque()

for i in range(n):
    cmd = sys.stdin.readline().rstrip()
    if len(cmd)>5:
        cmd, x = cmd.split()
    
    if cmd == "push":
        queue.append(x)
    elif cmd == "pop":
        if len(queue) != 0:
            print(queue.popleft())
        else:
            print(-1)
    elif cmd == "size":
        print(len(queue))
    elif cmd == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif cmd == "front":
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    elif cmd == "back":
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)
