import sys
input = sys.stdin.readline

n = int(input())

building = []
cnt = 0
stack = []

# 몇개의 빌딩이 나를 볼 수 있는지 세아리기
# 내가 몇개의 빌딩을 볼 수 있는지 세아리기 X
for i in range(n):
    tmp = int(input())
    while stack and stack[-1]<=tmp: # 스택 top이 나보다 같거나 작으면 걔 빼내기 == 나보다 큰것만 남길거임
        stack.pop()
    if stack and stack[-1]>tmp:
        cnt += len(stack) # 나보다 큰것들만 남음 == 걔네는 나를 볼 수 있음
    stack.append(tmp)

print(cnt)