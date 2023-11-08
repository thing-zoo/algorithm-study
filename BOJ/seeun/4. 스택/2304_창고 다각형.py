import sys
input = sys.stdin.readline

n = int(input())
height = [0] * 1001
maxheight = 0
maxloc = []
for _ in range(n):
    i, h = map(int, input().rstrip().split())
    height[i] = h
    if h > maxheight:
        maxheight = h
        maxloc = [i]
    elif h == maxheight:
        maxloc.append(i)

maxloc.sort() # 위치 정렬 -> 양옆으로 내려가면서 지붕 짓기

# 1. 가장 앞쪽에 있는 가장 큰 기둥 왼쪽부분
ans = 0
width = 0
stack = []
for i in range(maxloc[0]):
    if height[i] != 0:
        if stack:
            if stack[-1] < height[i]: # 현재 기둥이 이전보다 크면 -> 이전까지 최대높이*너비
                tmph = stack.pop()
                ans += width * tmph
                stack.append(height[i])
                width = 0
        else: # 스택 비어있으면 넣기만 함
            stack.append(height[i])
    if stack: # 곱할 높이가 있을 때만 너비 +1
        width += 1

if stack:
    ans += stack[-1]*width

# 2. 가장 뒤쪽에 있는 가장 큰 기둥 오른쪽부분
width = 0
stack = []
for i in range(1000, maxloc[-1], -1):
    if height[i] != 0:
        if stack:
            if stack[-1] < height[i]:
                tmph = stack.pop()
                ans += width * tmph
                stack.append(height[i])
                width = 0
        else:
            stack.append(height[i])
    if stack:
        width += 1
if stack:
    ans += stack[-1]*width

# 3. 가장 높은 첫번째~마지막 기둥 너비 * 높이
ans += maxheight * (maxloc[-1]-maxloc[0] +1)
print(ans)