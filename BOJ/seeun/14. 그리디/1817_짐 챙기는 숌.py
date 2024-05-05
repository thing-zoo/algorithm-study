n, m = map(int, input().split())
cnt = 0 # 박스 게수
weight = 0 # 현재 박스 무게

if n > 0:
    books = list(map(int, input().split()))
    for i in range(n):
        if weight + books[i] <= m: # 현재 책을 담을 수 있으면 담기
            weight += books[i]
        else: # 현재 책을 못담는 상황이면
            cnt += 1 # 박스 하나 추가하고
            weight = books[i] # 현재 박스 무게: 현재 책 무게
    cnt += 1 # 마지막 박스 카운트

print(cnt)