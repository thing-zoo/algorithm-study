# 다리길이 n, 가로등 개수 m, 위치 x
# m <= n <= 1e5, nlogn로 해결해야함
n = int(input())
m = int(input())
x = list(map(int, input().split()))

start = 1
end = n
result = 0 # 최소 높이
while start <= end:
    h = (start + end)//2
    
    check = True # 가로등 설치 가능 여부
    light = [(x[i]-h, x[i]+h) for i in range(m)] # 가로등별 비춰지는 범위
    for i in range(m):
        if i == 0 and light[i][0] > 0:
            check = False
            break
        if i == m-1 and light[i][1] < n:
            check = False
            break
        if i > 0 and light[i-1][1] < light[i][0]:
            check = False
            break
    
    if check:
        end = h-1
        result = h
    else:
        start = h+1
print(result)