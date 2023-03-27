import sys
n = int(sys.stdin.readline())
h = [ int(sys.stdin.readline()) for _ in range(n) ]
ans = 0
stack = []
for i in h:
    while stack and stack[-1] <= i:
        stack.pop()
    if stack:
        ans += len(stack)
    stack.append(i)
print(ans)
