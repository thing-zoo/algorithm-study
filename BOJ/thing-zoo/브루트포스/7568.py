n = int(input())
data = [ [i] + list(map(int, input().split())) for i in range(n)]

for i in range(n):
    count = 0
    for j in range(n):
        if i == j: continue
        if data[i][1] < data[j][1] and data[i][2] < data[j][2]:
            count += 1 # 자신보다 덩치 큰 사람 수 세기
    print(count + 1, end=' ') # 자신보다 덩치 큰 사람 수 + 1 이 등수