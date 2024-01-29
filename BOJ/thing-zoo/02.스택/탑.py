import sys

n = int(sys.stdin.readline())
h = list(map(int, sys.stdin.readline().split())) # 탑들의 높이
stack = [] # 탑의 인덱스 저장
answer = [0] * n 

for i in range(n): # 앞에서부터 돌면서
    while stack and h[stack[-1]] < h[i]: # 현재탑의 높이보다 작은 탑이면
        stack.pop() # 제거
    if stack: # 남은 탑이 있으면
        answer[i] = stack[-1] + 1 # 탑의 번호 넣기
    stack.append(i)

print(*answer)