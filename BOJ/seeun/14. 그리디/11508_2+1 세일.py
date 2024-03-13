import sys
input = sys.stdin.readline
n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

# 최대한 비싼 물품을 무료로 받기 위해 내림차순으로 정렬
nums.sort(reverse = True)
ans = 0
for i in range(n):
    if (i+1) % 3 != 0: # +1 물품은 무료로 받기
        ans += nums[i]
print(ans)