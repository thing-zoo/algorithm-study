n = int(input())
nums = list(map(int, input().split()))

nums.sort()
ans = 0
for i in range(n):
    ans += sum(nums[:i+1])
print(ans)