import sys
input = sys.stdin.readline

nums = []
tmp = list(map(int, input().rstrip().split()))
if len(tmp)>1:
    n = tmp[0]
    for i in range(1, len(tmp)):
        num = (str(tmp[i])[::-1])

        nums.append(int(num))

while len(nums)<n:
    tmp = list(map(int, input().rstrip().split()))
    for i in range(len(tmp)):
        num = str(tmp[i])[::-1]
        nums.append(int(num))
    # nums += tmp
nums.sort()
print("\n".join(map(str, nums)))