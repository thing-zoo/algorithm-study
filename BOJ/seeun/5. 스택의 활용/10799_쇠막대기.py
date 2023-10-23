tmp = list(input())
stack = []
ans = 0
for i in range(len(tmp)):
    if tmp[i] == ')':
        if i > 0 and tmp[i-1] == '(': # 레이저부분
            stack.pop() # 레이저인 ( pop
            ans += len(stack)
        else: # 한 막대기가 끝난거면 마지막 조각 추가
            ans += 1
            stack.pop() # 시작 ( 빼기
    else:
        stack.append('(')

print(ans)