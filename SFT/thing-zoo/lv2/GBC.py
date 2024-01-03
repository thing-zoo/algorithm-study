n, m = map(int, input().split())
limit = [list(map(int, input().split())) for _ in range(n)]
user = [list(map(int, input().split())) for _ in range(m)]
answer = 0 # 초과된 속도 최댓값
for i in range(m):
    for j in range(n):
        if limit[j][0] == 0: continue # 이미 확인한 구간
        a, b = user[i][0], limit[j][0]
        limit[j][0] = max(b-a, 0) # 확인한 거리만큼 제거
        user[i][0] = max(a-b, 0)
        answer = max(user[i][1]-limit[j][1], answer) # 초과된 속도 비교
        if user[i][0] == 0: break # 남은 거리가 없으면 종료
print(answer)