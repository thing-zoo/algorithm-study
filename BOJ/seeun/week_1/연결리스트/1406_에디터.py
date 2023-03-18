import sys
string = list(sys.stdin.readline().strip())
n = int(sys.stdin.readline())
left = string
right = []

for i in range(n):
    cmd = sys.stdin.readline().strip()
    if len(cmd)>1:
        cmd, s = cmd.split()

    if cmd == "L":
        right = left[-1:]+right[:]
        left = left[:-1]
    elif cmd == "D":
        left = left[:] + right[:1]
        right = right[1:]
    elif cmd == "B":
        if len(left) > 0:
            left.pop()
    elif cmd == "P":
        left.append(s)
    print(left, right)


print(*left,*right, sep="")