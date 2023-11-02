import sys
input = sys.stdin.readline
w, n = map(int, input().rstrip().split())
metals = [tuple(map(int, input().rstrip().split())) for _ in range(n)]
metals.sort(key=lambda x: x[1], reverse=True) # 무게당 가치가 높은순 정렬

answer = 0 # 최대 가치
for m, p in metals: # 정렬 순으로 넣는다
    if m <= w: # 남은 무게이하면
        w -= m # 넣고
        answer += p*m 
    else: # 마지막 차례
        answer += p*w 
        break # 종료
print(answer)
