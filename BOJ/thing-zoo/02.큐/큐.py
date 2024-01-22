import sys
q = []
n = int(input())
for _ in range(n):
    order = sys.stdin.readline().split()
    if order[0] == "push":
        q.append(order[1])
    elif order[0] == "pop":
        if not q:
            print(-1)
        else:
            print(q.pop(0))
    elif order[0] == "size":
        print(len(q))
    elif order[0] == "empty":
        if not q:
            print(1)
        else:
            print(0)
    elif order[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    else: # back
        if q:
            print(q[-1])
        else:
            print(-1)