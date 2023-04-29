n = int(input())
m = int(input())
vip = []
for _ in range(m):
    vip.append(int(input()))

if m == n or m-1 == n: # 모든 사람이 vip일때, 한명빼고 다 vip일때
    print(1)
else:
    d = [0] * (n+1)
    d[0] = 1
    d[1] = 1
    # 중간에 vip가 없는 좌석의 길이가 i 일때 경우의 수
    for i in range(2, n+1):
        d[i] = d[i-1] + d[i-2]

    res = 1 # 결과값 저장
    idx = 1 # 시작인덱스
    # vip사이사이 좌석의 길이의 경우의 수를 구해서 곱함
    for i in range(m):
        res *= d[vip[i]-idx]
        idx = vip[i]+1
    res *= d[(n+1)-idx]
    print(res)