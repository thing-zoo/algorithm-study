# 더 빠르고 깔끔한 코드
n = int(input()) # 크레인 개수
limit = list(map(int, input().split())) # 크레인별 무게제한
m = int(input()) # 박스 개수
weight = list(map(int, input().split())) # 박스별 무게
limit.sort(reverse=True)
weight.sort(reverse=True)

if limit[0] < weight[0]: # 최대 무게 제한보다 최대 박스무게가 더 크면
    print(-1) # 불가능
else:
    answer = 0 # 모든 박스 싣는데 드는 최소 시간
    while weight: # 박스 다 실을때까지
        for l in limit: # 크레인에 대해
            if weight and l < weight[-1]: # 실을 수 있는 박스 없으면
                continue # 넘기기
            for w in weight: # 박스에 대해
                if l >= w: # 실을 수 있으면
                    weight.remove(w) # 제거
                    break
        answer += 1
    print(answer)