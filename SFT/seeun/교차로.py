import sys
from collections import deque
input = sys.stdin.readline
n = input()
n = int(n)
hq = []
queue = [deque() for _ in range(4)]
for i in range(n):
    a, b = input().split()
    a = int(a)
    queue[ord(b)-ord('A')].append([i, a]) # 어느 교차로, 차번호, 들어오는 시각

time = 0
ans = [-1] * n
while queue[0] or queue[1] or queue[2] or queue[3]: # 모든 교차로에 차가 없을 때까지
    gotime = float('inf')
    cars = [0] * 4 # 현재 시간에 각각의 교차로에서 나가야할 자동차 수

    for i in range(4): # 네개의 교차로 중에 현재 나갈 준비가 된 자동차 찾기
        if queue[i]: # i 교차로에 차가 있으면
            gotime = min(gotime, queue[i][0][1]) # 나갈 시간 갱신(더 먼저 나가야하는 자동차 시간으로 갱신)
            if queue[i][0][1] <= time: # i교차로의 첫번째 자동차 나갈 시간이 현재시간보다 이르면
                cars[i] += 1 # i번째 교차로의 나갈 차 대수 +1

    wait = sum(cars) # 모든 교차로에서 나갈 준비하고 있는 자동차 숫자
    if wait == 4: # 모든 교차로에서 대기하고 있으면 교착상태
        break
    elif wait == 0: # 아무도 대기하고 있지 않으면 패스
        time = gotime
        continue

    for i in range(4):
        if cars[i] and cars[i-1] == 0: # 오른쪽 교차로에 차가 없는 자동차만 나갈 수 있음
            num, t = queue[i].popleft()
            ans[num] = time # 자동차가 나간 시각 저장

    time += 1

print("\n".join(map(str, ans)))