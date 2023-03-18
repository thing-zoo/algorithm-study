import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

stack = []
res = [-1] * n
for i in range(n-1, -1, -1):
    now = nums[i]

    if len(stack) != 0:
        while stack and stack[-1]<=now:
            stack.pop()
    
    if stack:
        res[i] = stack[-1]
    
    stack.append(now)
    # print(res, stack)

# res.reverse()
print(*res)