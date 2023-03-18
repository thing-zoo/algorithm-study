import sys 
n = int(input())

queue = []

for i in range(n):
    cmd = sys.stdin.readline().rstrip()
    if len(cmd)>5:
        cmd, x = cmd.split()
    
    if cmd == "push":
        queue.append(x)
    elif cmd == "pop":
        if len(queue) != 0:
            print(queue[0])
            del queue[0]
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
            print(queue[len(queue)-1])
        else:
            print(-1)
