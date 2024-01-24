a, b, c, m = map(int, input().split())
work = 0
tire = 0
for _ in range(24): # 24시간 동안 일하기
    if tire + a > m: # 피로도가 m 이상이면
        tire = max(0, tire-c) # 하루 쉬기
    else:
        tire += a # 피로도 a 만큼 쌓임
        work += b # b만큼 일하기

print(work)