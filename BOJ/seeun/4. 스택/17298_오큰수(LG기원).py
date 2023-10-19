n = int(input())
nums = list(map(int, input().split()))
nums.reverse()
stack = []
ans = []
for i in range(n):
    while stack and stack[-1] <= nums[i]:
        stack.pop()
    if stack:
        ans.append(stack[-1])
    else:
        ans.append(-1)
    stack.append(nums[i])
ans.reverse()
print(*ans)