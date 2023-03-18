import sys

n = int(input())

stack = []

for i in range(n):
    cmd = sys.stdin.readline().rstrip()
    if len(cmd)>5:
        cmd, num = cmd.split()
    
    if cmd == "push":
        stack.append(num)
    elif cmd == "pop":
        if len(stack)>0:
            print(stack.pop())
        else:
            print(-1)
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif cmd == "top":
        if len(stack)>0:
            print(stack[len(stack)-1])
        else:
            print(-1)
