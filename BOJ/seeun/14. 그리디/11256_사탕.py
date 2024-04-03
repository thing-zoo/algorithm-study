import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    J, N = map(int, input().split())
    boxes = [list(map(int, input().split())) for _ in range(N)]
    boxes.sort(key = lambda x:-x[0]*x[1]) # 상자 크기 기준 내림차순 정렬
    
    cnt = 0
    total = J
    for b in boxes:
        if b[0] * b[1] <= total: # 박스 크기 <= 남은 사탕 수
            total -= b[0] * b[1] # 들어가는 만큼만 담기
            cnt += 1 # 상자 수 +1
        else: # 박스 크기 > 남은 사탕 수
            total = 0 # 남은 사탕 없음
            cnt += 1 # 상자수 +1

        # 남은 사탕이 없으면 종료
        if total <= 0:
            break
    print(cnt)