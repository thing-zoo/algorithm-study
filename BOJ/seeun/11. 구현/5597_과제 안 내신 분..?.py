nums = [False] * 31 # 초기값 1~30 False로
nums[0] = True # 0은 안쓸거라서 True로
for _ in range(28):
    n = int(input())
    nums[n] = True # 제출한 사람
ans = nums.index(False) # 가장 먼저 나오는 제출 안한 사람
nums[ans] = True
print(ans)
print(nums.index(False)) # 두번째 제출 안한사람
