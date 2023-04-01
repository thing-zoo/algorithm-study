# 4:35 # 16%
import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().strip()[1:-1].split(',')
    if n == 0:
        arr = []
    q = deque(arr)
    flag = 0 # 뒤집기
    error = 0
    for i in p:
        if i == "R":
            flag = not flag
        else: # "D"
            if q:
                if flag:
                    q.pop()
                else:
                    q.popleft()
            else:
                error = 1
                break
        
    if error:
        print("error")
    else:
        if flag:
            arr = "[" + ",".join(reversed(q)) + "]"
        else: 
            arr = "[" + ",".join(q) + "]"
        print(arr)