import math
n = int(input())
nums = list(map(int, input().split()))
ans = max(nums) # 가장 큰 숫자를 기준으로 둠
nums.sort()
for i in range(n-1): 
    ans += nums[i]/2 # 나머지 음료를 반만 더함

print(ans if math.floor(ans) != ans else int(ans)) # 정수이면 소수점 없이 출력