# h: 세로, w: 가로, n: 세로 간격, m: 가로 간격
h, w, n, m = map(int, input().split())
x = 0 # 한 세로줄에 앉을 수 있는 인원 수
y = 0 # 한 가로줄에 앉을 수 있는 인원 수
for _ in range(0, h, n+1):
    x += 1
for _ in range(0, w, m+1):
    y += 1
print(x*y)