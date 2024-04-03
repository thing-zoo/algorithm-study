import sys
input = sys.stdin.readline
n = int(input())
circle = []
for i in range(n):
    a, b = map(int, input().split())
    circle.append([a-b, i]) # i원의 왼쪽 점
    circle.append([a+b, i]) # i원의 오른쪽 점
circle.sort() # 왼쪽 -> 오른쪽 점 순서대로 정렬

stack = []
for c in circle:
    if stack:
        if stack[-1][1] == c[1]: # 스택 탑에 있는 점의 짝꿍이 나타났으면
            stack.pop() # 해당 원의 왼쪽 점 pop
        else:
            stack.append(c) # 가장 위에 있는 점과 짝이 맞지 않으면 push
    else:
        stack.append(c) # 스택이 비었으면 그냥 push

if stack: # 스택이 비어있지 않으면 원이 교점이 생기는 경우
    print('NO')
else:
    print('YES')
