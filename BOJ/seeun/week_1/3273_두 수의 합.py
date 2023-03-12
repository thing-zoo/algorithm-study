import sys
n = int(input())
nums = list(map(int, sys.stdin.readline().split()))
x = int(input())

check = [0] * (x+2)
cnt = 0
for i in range(n):
    if nums[i]<x:
        check[nums[i]] = 1 #일단 체크 -> 빼기 한게 0이면 
        if check[x - nums[i]] == 1 and x - nums[i] != nums[i]:
            cnt += 1
        
print(cnt)