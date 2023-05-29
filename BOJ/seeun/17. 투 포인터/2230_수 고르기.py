n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]
nums.sort()
r = 0
ans = float("inf")
for l in range(n):
    while r<n and nums[r]-nums[l] < m: # 두 수의 차가 m보다 크거나 같아지면 멈춤
        r += 1
    if r == n:
        break
    ans = min(ans, nums[r]-nums[l])

print(ans)