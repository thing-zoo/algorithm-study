import sys
input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

d = [0]*1000001
d[1] = 1
d[2] = 2
d[3] = 4
for i in range(4, max(nums)+1):
    d[i] = (d[i-1] + d[i-2] + d[i-3])%1000000009

for i in range(n):
    num = nums[i]
    # print(d[num]%1000000009)
    sys.stdout.write(str(d[num]%1000000009))
    sys.stdout.write("\n")