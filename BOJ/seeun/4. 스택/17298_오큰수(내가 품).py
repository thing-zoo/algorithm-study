import sys
n = int(input())
nums = list(map(int, sys.stdin.readline().split()))

stack = []
nums.reverse() # 뒤에서 부터 담을거임
ans = []

for i in range(n):
    while stack and stack[-1]<=nums[i]: # 스택 top이 나보다 작거나 같으면 pop, 나보다 큰 수 나오면 멈춤
        stack.pop()

    if stack: # 스택에 뭐가 남아있으면 그게 나랑 가장 가까운 큰 수
        ans.append(stack[-1])
    else: # 아무것도 없으면 내가 제일 큰 수
        ans.append(-1)
    stack.append(nums[i])

ans.reverse()
print(*ans)