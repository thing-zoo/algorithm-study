n, l = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
for i in range(n):
    if nums[i] <= l: # 나보다 작거나 같으면
        l += 1 # 먹고 길이 +1
    else:
        break
print(l)