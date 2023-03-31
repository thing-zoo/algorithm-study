from collections import deque
import sys
input = sys.stdin.readline

n,l = map(int, input().rstrip().split())

nums = list(map(int, input().split()))
comp = deque()

for i in range(n):
    
    while comp and comp[-1][1]>nums[i]:
        comp.pop()
    comp.append((i, nums[i])) # index, value

    while comp and comp[0][0] < i-l+1:
        comp.popleft()
    
    print(comp[0][1], end=" ")