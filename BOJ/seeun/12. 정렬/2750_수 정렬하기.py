n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

nums.sort()
print("\n".join(map(str, nums)))