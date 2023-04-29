n = int(input())
nums = list(map(int, input().split()))

d = [0]*n
d[0] = nums[0]
for i in range(1, n):
    for j in range(i): # 0~현재수 전 까지 숫자 갱신함 
        if nums[j]<nums[i]:
            d[i] = max(d[i], d[j] + nums[i])
        else: # 앞 숫자가 나보다 크면
            d[i] = max(d[i], nums[i])
print(max(d))
