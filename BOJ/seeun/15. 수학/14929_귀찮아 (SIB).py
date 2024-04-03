n = int(input())
nums = list(map(int, input().split()))

ans = 0
total = sum(nums)
for i in range(n-1):
    total -= nums[i]
    ans += total * nums[i] # i<x인 숫자를 모두 더해서 i와 곱함

print(ans)