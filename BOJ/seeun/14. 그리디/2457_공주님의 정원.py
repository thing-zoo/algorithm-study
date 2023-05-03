import sys
input = sys.stdin.readline

n = int(input())
flower = []
for _ in range(n):
    a, b, c, d = map(int, input().rstrip().split())
    flower.append([a*100+b, c*100+d])

flower.sort()

end = 301
cnt = 0
while flower: 
    # 현재 꽃 지는 시간이 12월 1일 이후(그만심어도 됨)이거나, 꽃과 꽃 기간이 이어지지않을 경우
    if end>=1201 or end < flower[0][0]:
        break

    tmp = -1
    # 현재 꽃의 지는날 이전에 피고 제일 늦게 지는 것 뽑기
    for _ in range(len(flower)):
        if flower[0][0] <= end: # 피는 날이 지금 꽃이 지기 전이면
            tmp = max(tmp, flower[0][1]) # 그중에 제일 늦게까지 피어있는 꽃 날짜 저장
            flower.remove(flower[0]) # 확인했으니까 지우기
        else:
            break
    end = tmp # 현재꽃 이어서 심을 꽃의 지는 날 저장
    cnt += 1
if end < 1201:
    print(0)
else:
    print(cnt)
        