n = int(input())
nums = list(map(int, input().split()))
nums_reverse = list(reversed(nums))
d1 = [1] * n
d2 = [1] * n
ans = 0

for i in range(1, n):
    for j in range(i):
        if nums[j] < nums[i]: # 가장 긴 증가하는 수열
            d1[i] = max(d1[i], d1[j] + 1)
        if nums_reverse[j] < nums_reverse[i]: # reversed 수열에서 가장긴 증가하는 수열 == 원본 수열에서 가장 긴 감소하는 수열
            d2[i] = max(d2[i], d2[j] + 1)

# 원본 nums를 뒤집었기 때문에 결과도 뒤집어야함
d2.reverse()

for i in range(n):
    ans = max(d1[i] + d2[i], ans)

print(ans-1)
