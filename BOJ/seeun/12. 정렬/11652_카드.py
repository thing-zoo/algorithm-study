n = int(input())

nums = {}
for _ in range(n):
    tmp = int(input())
    if tmp not in nums:
        nums[tmp] = 1
    else:
        nums[tmp] += 1

print(sorted(nums.items(), key=lambda x:(-x[1], x[0]))[0][0])