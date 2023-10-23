import sys
from collections import deque
input = sys.stdin.readline
S = input().rstrip()
n = int(input().rstrip())
left = list(S) # 커서 왼쪽에 있는 문자들 - 초기: S
right = deque() # 커서 오른쪽에 있는 문자

for _ in range(n):
    cmd = input().rstrip()

    if len(cmd) > 1:
        P, x = cmd.split()
        left.append(x)
    elif left and cmd == "L": # 커서 왼쪽 이동
        right.appendleft(left.pop()) # 왼쪽 끝 문자를 오른쪽 첫번째에 추가    
    elif right and cmd == "D": # 커서 오른쪽 이동
        left.append(right.popleft()) # 오른쪽 첫번째 문자를 왼쪽에 추가
    elif left and cmd == "B":
        left.pop()

print("".join(left), "".join(right), sep="")

