from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    cmd = list(input().rstrip())
    m = int(input().rstrip())
    if m>1:
        nums = deque(map(int, input().strip('\[\]\n').split(',')))
    elif m == 0:
        nums = input()
        nums = deque()
    else:
        nums = input().strip('\[\]\n')
        nums = int(nums)
        tmp = [nums]
        nums = deque(tmp)
    check = True
    prev = True
    for i in range(len(cmd)):
        if cmd[i] == "R":
            prev = not(prev)
        elif cmd[i] == "D":
            if prev == True:
                if len(nums) > 0:
                    nums.popleft()
                else:
                    print("error")
                    check = False
                    break   
            else:    
                if len(nums) > 0:
                    nums.pop()
                else:
                    print("error")
                    check = False
                    break
    if check:
        print("[", end="")
        if prev:
            print(*nums, sep=",", end="")
        else:
            nums.reverse()
            print(*nums, sep=",", end="")
        print("]")
    