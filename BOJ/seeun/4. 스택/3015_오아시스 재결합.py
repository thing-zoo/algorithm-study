import sys
input = sys.stdin.readline
n = int(input())
stack = []
cnt = 0
for i in range(n):
    h = int(input())
    while stack and stack[-1][0]<h: # 스택탑이 나보다 작으면 pop
        cnt += stack.pop()[1]
        
    if not stack: # 비어있는 스택에는 그냥 넣기
        stack.append((h, 1))
        continue
    
    # 스택이 비어있지 않으면
    if stack[-1][0] == h: 
        tmp = stack.pop()[1]
        cnt += tmp

        if stack:
            cnt += 1

        stack.append((h, tmp+1))

    else: # 스택탑이 나보다 큰 경우
        cnt += 1
        stack.append((h, 1))
    # print(stack, cnt)
print(cnt)
