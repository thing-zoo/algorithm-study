t = int(input())
nums = [1]*(1000001)

nums[0] = 0
nums[1] = 0
for i in range(2, 1000001):
    if nums[i]:
        for j in range(i+i, 1000001, i):
            nums[j] = 0

for _ in range(t):
    n = int(input())
    cnt = 0
    for i in range(2, n//2+1): # 순서만 다른 것은 같은 파티션임 -> 반만 확인하면 됨
        if nums[n-i] and nums[i]:
            cnt += 1
    print(cnt)