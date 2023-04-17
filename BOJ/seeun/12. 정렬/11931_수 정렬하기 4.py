import sys
input = sys.stdin.readline
n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

nums.sort(reverse=True)
print("\n".join(map(str, nums)))