import sys
from itertools import permutations
n, m, k = map(int, input().split())
w = list(map(int, input().split()))
answer = 50*50 # 최소한의 택배 무게
for order in permutations(range(n)): # 레일 순서의 모든 경우의 수
    total = 0 # 총 일한 무게
    bucket = 0 # 현재 바구니의 무게
    count = 0 # 일한 횟수
    i = 0
    while count < k: # k번 일할때까지
        if bucket + w[order[i]] <= m: # 바구니 무게를 넘어가기 전까지
            bucket += w[order[i]] # 추가
            total += w[order[i]]
            i = (i+1)%n
        else: # 초과되면
            count += 1 # 카운트
            bucket = 0 # 바구니 초기화
        if answer <= total: # 현재 최소무게 이상이면
            break # 볼 필요 없으므로 종료
    answer = min(answer, total)
print(answer)