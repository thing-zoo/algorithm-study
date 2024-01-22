import sys
input = sys.stdin.readline
n = int(input())
circles = []
for i in range(n):
    x, r = map(int, input().split())
    circles.append((x-r, i))
    circles.append((x+r, i))
circles.sort()

stack = []
for c in circles:
    if stack:
        if stack[-1][1] == c[1]:
            stack.pop()
    stack.append(c)
    
if stack:
    print('NO')
else:
    print('YES')