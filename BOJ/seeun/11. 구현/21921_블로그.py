n, x = map(int, input().split())
nums = [0]+list(map(int, input().split()))
total = sum(nums[1:x])
maxsum = 0
maxcnt = 0
for i in range(x, n+1):
    total += nums[i] # 마지막 값 더하기
    if total > maxsum:
        maxsum = total
        maxcnt = 1
    elif total == maxsum:
        maxcnt += 1
    total -= nums[i-x+1] # 처음 값 빼기

if maxsum:
    print(maxsum)
    print(maxcnt)
else:
    print("SAD")