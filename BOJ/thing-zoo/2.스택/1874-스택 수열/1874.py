n = int(input())
cur = 1 # 스택에 넣을 번호
stack = []
answer = []
for _ in range(n):
    x = int(input())
    while cur <= x: # cur가 x에 도달할때까지
        stack.append(cur) # 삽입
        answer.append('+')
        cur += 1
    if stack[-1] == x: # top이 x면
        stack.pop() # 제거
        answer.append('-')
    else: # 아니면
        break # 불가능
if stack: # 스택에 남아있으면
    print('NO') # 불가능
else:
    print('\n'.join(answer)) # 가능