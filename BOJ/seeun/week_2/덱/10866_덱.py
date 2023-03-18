from collections import deque
import sys

input = sys.stdin.readline

deq = deque()
n = int(input())

# push_back 1
# push_front 2
# front
# back
# size
# empty
# pop_front
# pop_back
for i in range(n):
    cmd = input().rstrip()
    if cmd[:9] == "push_back" or cmd[:10] == "push_front":
        cmd, x= cmd.split()

    if cmd == "push_front":
        deq.appendleft(x)
    elif cmd == "push_back":
        deq.append(x)
    elif cmd == "pop_front":
        if len(deq)>0:
            print(deq.popleft())
        else:
            print(-1)
    elif cmd == "pop_back":
        if len(deq)>0:
            print(deq.pop())
        else:
            print(-1)
    elif cmd == "front":
        if len(deq)>0:
            print(deq[0])
        else:
            print(-1)
    elif cmd == "back":
        if len(deq)>0:
            print(deq[-1])
        else:
            print(-1)
    elif cmd == "size":
        print(len(deq))
    elif cmd == "empty":
        if len(deq)>0:
            print(0)
        else:
            print(1)
