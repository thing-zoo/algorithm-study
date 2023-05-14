t = int(input())
nums = [1]*(10001)

nums[0] = 0
nums[1] = 0
for i in range(2, 10001):
    if nums[i]:
        for j in range(i+i, 10001, i):
            nums[j] = 0

for _ in range(t):
    n = int(input())
    for i in range(n//2+1, -1, -1): # 숫자 차이가 작은것을 출력 -> 큰 숫자부터 확인하기
        if nums[n-i] and nums[i]:
            if n-i<i:
                print(n-i, i)
            else:
                print(i, n-i)
            break