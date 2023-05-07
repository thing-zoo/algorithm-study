from collections import deque
n, c = map(int, input().split())
m = int(input())
box = []
for _ in range(m):
    box.append(list(map(int, input().split())))

box.sort(key=lambda x:(x[1], x[0], x[2]))

ans = 0
truck = deque()
remain = [c] * (n+1)
for i in range(m): # 택배 개수만큼
    capacity = c
    for j in range(box[i][0], box[i][1]): # 현재 물건의 시작지 도착지 사이에서
        capacity = min(capacity, remain[j]) # 실을 수 있는 가장 작은 값
    capacity = min(capacity, box[i][2]) #실을 수 있는 만큼 싣기

    for j in range(box[i][0], box[i][1]):
        remain[j] -= capacity # 그 마을에 싣고 갈 수 있는 용량을 지금 실은 만큼 빼기
    ans += capacity
print(ans)