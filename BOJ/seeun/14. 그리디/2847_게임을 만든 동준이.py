n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

ans = 0
for i in range(n-1, 0, -1): # 뒤에서부터
    if nums[i-1] >= nums[i]: # 앞에있는 수가 나보다 크면
        ans += (nums[i-1] - nums[i])+1 # 얼마나 빼야하는지 더하고
        nums[i-1] -= (nums[i-1]-nums[i])+1 # 숫자를 수정해줌
print(ans)