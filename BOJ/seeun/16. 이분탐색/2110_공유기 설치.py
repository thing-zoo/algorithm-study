import sys
input = sys.stdin.readline
n, c = map(int, input().rstrip().split())
house=[]
for _ in range(n):
    house.append(int(input()))
house.sort()
# print(house)

s = 1
e = house[-1]-house[0]
maxlen = -1
while s<=e:
    m = (s+e)//2
    cnt = 1
    prevhouse = house[0]
    for h in range(1, len(house)): 
        if house[h]-prevhouse>=m: # 현재 집과 앞집 거리가 m 일때 
            cnt += 1
            prevhouse = house[h]
            # print(house[h])
    if cnt >= c: # 집사이의 거리가 최대 m일 때 공유기 설치 개수가 c개 일때
        s  = m+1
        maxlen = m # 최대 길이를 갱신
    else:
        e = m-1
print(maxlen)