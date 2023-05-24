n, m = map(int, input().split())
nums = [0]
nums.extend(list(map(int, input().split())))
for i in range(1, len(nums)):
    nums[i] += nums[i-1]
n += 1
r = 0
ans = 0
for l in range(n):
    while r<n and nums[r]-nums[l] < m:
        r += 1
    if r == n:
        break
    if nums[r]-nums[l] == m:
        ans += 1
print(ans)