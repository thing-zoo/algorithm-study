n, c = map(int, input().split())

tmp = list(map(int, input().split()))
nums = {}
for i in range(n):
    if tmp[i] not in nums:
        nums[tmp[i]] = 1
    else:
        nums[tmp[i]] += 1

tmp = sorted(nums.items(), key=lambda x:-x[1])
for i in range(len(tmp)):
    print((str(tmp[i][0])+" ")*tmp[i][1], end="")