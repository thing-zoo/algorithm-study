n = int(input())
nums = list(map(int, input().split()))
m = int(input())

nums.sort()
s = 1
e = nums[-1]
ans = 0
while s<=e:
    mid = (s+e)//2
    cnt = 0
    for i in range(n):
        cnt += min(mid, nums[i]) 
    if cnt > m:
        e = mid-1
    else:
        s = mid + 1
        ans = mid
print(ans)