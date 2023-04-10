from collections import deque
n, length, maxweight = map(int, input().split())
trucks = list(map(int, input().split()))
bridge = deque()
time  = deque()
nowTime = 0
i = 0
while True:
    # 이미 다리 다 지났는지 체크 = 지금 시간 - time == length
    # 들어갈 수 있는지 체크 = sum
    if i>0 and len(bridge) == 0: # 다 들어갔고 다리에 아무도 없으면
        break
    if bridge and nowTime - time[0] == length: # 다리 다 건넌 애들은 빼주기
        bridge.popleft()
        time.popleft()
    if i>=n: # 다리가 다 들어갔으면 시간만 증가시켜주기
        nowTime+= 1
        continue
    if sum(bridge)+trucks[i]<= maxweight: # 다음 트럭 들어갈수 있는지 체크
        bridge.append(trucks[i])
        time.append(nowTime)
        i += 1

    nowTime += 1

print(nowTime)