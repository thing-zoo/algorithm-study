import sys
input = sys.stdin.readline
n = int(input())
stack = []
answer = 0
for _ in range(n):
    a = int(input())
    if not stack:
        stack.append(a)
print(answer)