nums = list(map(int, input().split()))
flag = [False] * 3
for i in range(3):
    if nums[i] % 2 == 1:
        flag[i] = True

if flag.count(True) == 2: # 홀수가 두개이면 홀수만 곱함
    res = 1
    for i in range(3):
        if flag[i]:
            res *= nums[i]
    print(res)
elif flag.count(True) == 1: # 홀수가 한개이면 그게 최대
    print(nums[flag.index(True)])
else: # 모두 홀수 혹은 짝수이면 다 곱하는게 최대
    print(nums[0] * nums[1] * nums[2])