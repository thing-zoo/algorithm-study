import math

n = input()
n = n.replace('9','6')
n = list(map(int, n))

nums = {}
for i in n:
    nums[i] = n.count(i)

if 6 in n:
    nums[6] = math.ceil(nums[6]/2)
print(max(nums.values()))