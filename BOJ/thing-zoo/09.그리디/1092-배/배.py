n = int(input()) # 크레인 개수
limit = list(map(int, input().split())) # 크레인별 무게제한
limit.sort()
m = int(input()) # 박스 개수
weight = list(map(int, input().split())) # 박스별 무게
weight.sort()

if limit[-1] < weight[-1]: # 최대 무게 제한보다 최대 박스무게가 더 크면
    print(-1) # 불가능
else:
    load = [0]*n # 실을 수 있는 박스 개수
    j = 0
    for i in range(m): # 박스를 순서대로
        while weight[i] > limit[j]: # 현재 무게제한보다 크면
            j += 1 # 다음 크레인
        load[j] += 1 # 추가
    answer = 0 # 모든 박스를 옮기는 데 드는 최소 시간
    while sum(load) > 0: # 다 옮길 때까지
        for i in range(n): # 크레인은 동시에 작동 가능
            if load[i]: # 옮길 게 있으면
                load[i] -= 1 # 옮기기
            else: # 없으면
                for j in range(i-1, -1, -1): # 이전 크레인중에
                    if load[j]: # 있으면
                        load[j] -= 1 # 옮기기
                        break
        answer += 1
    print(answer)