a, b = map(int, input().split())
nums = [0]*(b+1)

cnt = 0
i = 1
for j in range(1, b+1):
    nums[j] = i
    cnt += 1
    if cnt == i:
        cnt = 0
        i += 1
print(sum(nums[a:b+1]))