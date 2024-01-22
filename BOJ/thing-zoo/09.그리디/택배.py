n, c = map(int, input().split())
m = int(input())
delivery = [list(map(int, input().split())) for _ in range(m)]
delivery.sort(key=lambda x: x[1]) # 목적지를 기준으로 정렬
trucks = [0]*n # 각 마을 이동시 트럭의 박스수
max_boxes = 0 # 최대 박스 개수
for a, b, box in delivery:
    possible = box # 수용가능한 박스 수
    for i in range(a, b):
        if trucks[i] + possible > c: # 전체를 실었을때 초과된다면
            possible = min(c - trucks[i], possible) # 가능한 만큼만
    if possible: # 가능하다면
        for i in range(a, b):
            trucks[i] += possible # 싣기
        max_boxes += possible # 배달완료
print(max_boxes)
