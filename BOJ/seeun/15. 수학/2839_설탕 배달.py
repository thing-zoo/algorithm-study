n = int(input())

d = [9999]*(5000+1)
d[3] = 1
d[5] = 1

for i in range(6, n+1):
    for j in range(0, n+1, 3): # 3킬로 짜리를 *개 넣어서 만들 수 있는 최솟값
        d[i] = min(d[i], d[i-j]+d[j])
    for j in range(0, n+1, 5): # 5킬로 짜리를 *개 넣어서 만들 수 있는 최솟값
        d[i] = min(d[i], d[i-j]+d[j])

print(d[n] if d[n]!= 9999 else -1)