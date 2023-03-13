import sys
n = int(input())

nums = []
for i in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        nums.pop()
    else:
        nums.append(num)

print(sum(nums))