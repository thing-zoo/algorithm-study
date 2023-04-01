import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
stack = []
result = [0] * n

for i in range(n):
    while stack and data[stack[-1]] < data[i]:
        stack.pop()
    if stack:
        result[i] = stack[-1] + 1
    stack.append(i)

print(*result)