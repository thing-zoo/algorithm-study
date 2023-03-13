import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
ans = [0]*n
stack = []
for i in range(n-1, -1, -1):
    while stack and stack[-1] <= a[i]:
        stack.pop()
    if stack:
        ans[i] = stack[-1]
    else:
        ans[i] = -1
    stack.append(a[i])
print(*ans)