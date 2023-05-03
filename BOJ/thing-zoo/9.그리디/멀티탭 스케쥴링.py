n, k = map(int, input().split())
item = list(map(int, input().split()))
power = []
unplug = 0
for i in range(k):
    if item[i] in power: # 플러그가 이미 꽂혀있는 경우
        continue # 넘어가기
    if len(power) < n: # 꽂을 자리가 남아있는 경우
        power.append(item[i]) # 꽂기
    else: # 꽂을 자리가 없는 경우
        # 꽂혀있는 것들 중 이후에 안 사용하는 플러그
        # 전부 사용한다면 가장 나중에 사용할 플러그를 뽑기
        candi = []
        for p in power:
            idx = k + 1 # 사용안하는 거 확인용 초기화
            for j in range(i + 1, k):
                if p == item[j]:
                    idx = j
                    break
            candi.append([idx, p])
            candi.sort() # 가장 나중 인덱스 혹은 사용안하는 플러그 찾기 위해
        power.remove(candi[-1][1]) # 가장 마지막요소가 뽑을 플러그
        power.append(item[i])
        unplug += 1
print(unplug)