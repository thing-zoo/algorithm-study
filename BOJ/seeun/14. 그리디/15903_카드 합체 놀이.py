n, m = map(int, input().split())
nums = list(map(int, input().split()))

for i in range(m):
    nums.sort() # 오름차순으로 정렬
    nums[0], nums[1] = nums[0]+nums[1],nums[0]+nums[1] # 가장 작은 앞의 두수를 더함
print(sum(nums))