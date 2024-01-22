import sys
input = sys.stdin.readline
n = int(input())
circles = []
for _ in range(n):
    x, r = map(int, input().split())
    circles.append((x-r, x+r)) # 원의 처음과 끝 구간
circles.sort()

answer = 'YES'
a, b = circles[0]
for c, d in circles[1:]:
    if a == c or b == d or (c <= b and b < d): # 접하거나 교차
        answer = 'NO'
        break
    a, b = c, d
print(answer)