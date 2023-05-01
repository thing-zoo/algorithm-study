import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    # maxNum = 0
    # sell = []
    # ans = 0
    # for i in range(n):
    #     maxNum = max(nums[i:])
    #     if nums[i] == maxNum and len(sell) > 0: # 지금이 최대이고 산게 있으면 팔기
    #         for j in range(len(sell)):
    #             ans += maxNum-sell[j]
    #         sell = []
    #     elif nums[i] == maxNum: # 산게 없고 지금이 최대이면 넘어가기
    #         continue
    #     else:
    #         sell.append(nums[i])
    ans = 0
    maxNum = nums[-1]
    for i in range(n-2, -1, -1):
        if nums[i] < maxNum:
            ans += (maxNum - nums[i])
        else:
            maxNum = nums[i]
    print(ans)