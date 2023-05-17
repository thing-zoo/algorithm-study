n = int(input())
nums = list(map(int, input().split()))

s = 0
e = n-1
minus = False
ans = abs(nums[s]+nums[e])
while s<e:
    if nums[s] + nums[e] == 0:
        print(0)
        break
    if abs(nums[s]+nums[e]) <= ans:
        ans = abs(nums[s]+nums[e])
        # 출력할 때 음수인지 양수인지 표시해야하기 때문에
        if nums[s] + nums[e] < 0: # 음수이면 저장해둬야함
            minus = True
        else:
            minus = False
    if nums[s] + nums[e] < 0:
        s += 1
    else:
        e -=1
print(ans if not minus else -ans)