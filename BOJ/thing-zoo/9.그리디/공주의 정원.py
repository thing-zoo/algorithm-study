n = int(input())
flowers = []
for _ in range(n):
    m1, d1, m2, d2 = map(int, input().split())
    flowers.append([m1*100+d1, m2*100+d2]) # 날짜 비교를 위해 날짜형식으로 변형
flowers.sort() # 피는날이 빠른순 정렬

end_date = 301 # 이전 꽃의 지는날
latest_end_date = 0 # 가장 늦게 지는날
answer = 0 # 심어야할 꽃의 최소개수
i = 0
while i < n: # 모든 꽃에 대해
    while i < n: # 다음에 올 가장 늦게 지는 꽃 찾기
        start, end = flowers[i]
        if start > end_date or end_date > 1130: # 이전 꽃의 지는날이후거나 지는날이 11/30이후면
            break
        elif start <= end_date and end > latest_end_date: # 이전 꽃의 지는날 이전이면서 지는날이 가장 늦다면
            latest_end_date = end # 가장 늦게 지는날 갱신
        i += 1
    if latest_end_date: # 가장 늦게 지는날이 있으면
        end_date = latest_end_date # 이전 꽃의 지는날 갱신
        answer += 1 # 꽃 카운트
    if end_date > 1130 or start > end_date : # 지는날이 11/30이후거나 가능한 꽃이 없다면
        break # 종료
print(answer if end_date > 1130 else 0) # 모두 탐색했는데도 11/30이후까지 도달못한다면 0