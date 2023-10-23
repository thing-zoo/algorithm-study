n = int(input())
stairs = []
stairs.append(0)
for _ in range(n):
    stairs.append(int(input()))

d = [0] * (n+1)

if n <= 2: # 계단이 2칸 이하이면 모두 밟아도 됨
    ans = 0
    for i in range(1,n+1):
        ans += stairs[i]
    print(ans)
else: # 계단이 3칸 이상이면 dp 진행
    d[1] = stairs[1]
    d[2] = stairs[1] + stairs[2]
    d[3] = max(stairs[1]+stairs[3], stairs[2]+stairs[3]) # 1->3 2->3 중에 큰것
    for i in range(4, n+1):
        d[i] = max(d[i-3]+stairs[i-1] + stairs[i], d[i-2]+stairs[i]) # (3칸 전 최대 + 1칸 전 + 현재) vs (2칸 전 최대 + 현재)
    print(d[n])