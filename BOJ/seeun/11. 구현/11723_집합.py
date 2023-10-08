import sys
input = sys.stdin.readline
n = int(input())
S = 0
for i in range(n):
    line = input().rstrip()
    if line == 'all':
        S = 0b111111111111111111111
        continue
    elif line == 'empty':
        S = 0b0
        continue

    cmd, x = line.split()
    x = int(x)
    if cmd == 'add':
        S |= (0b1<<x)
    elif cmd == 'remove':
        S &= ~(0b1<<x)
    elif cmd == 'check':
        print(1 if (S & (0b1 <<x)) else 0)
    elif cmd == 'toggle':
        S ^= (0b1<<x) # 두 원소가 달라야 1

# 딕셔너리, 배열로 풀면 시간초과 ------------

# nums = [False] * 21
# # for i in range(1, 21):
# #     nums[i] = False

# for _ in range(n):
#     line = input()
#     if line == 'all':
#         # for i in range(1, 20):
#         #     nums[i] = True
#         nums = [True]*21
#         continue
#     elif line == 'empty':
#         # for i in range(1, 20):
#         #     nums[i] = False
#         nums = [False] * 21
#         continue

#     cmd, x = line.split()
#     x = int(x)
#     if cmd == 'add' and not nums[x]:
#         nums[x] = True
#     elif cmd == 'remove' and nums[x]:
#         nums[x] = False
#     elif cmd == 'check':
#         print(1 if nums[x] else 0)
#     elif cmd == 'toggle':
#         nums[x] = not nums[x]