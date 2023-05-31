import sys
input = sys.stdin.readline
s, e, q = input().rstrip().split()
s = s.replace(':', '')
e = e.replace(':', '')
q = q.replace(':', '')
d = {}
while True:
    try:
        time, name = input().rstrip().split()
        time = time.replace(':', '')
        if time <= s:
            d[name] = 1 # 입장 표시
        elif e <= time <= q:
            if name in d: # 입장했으면
                d[name] = 2 # 퇴장 표시
    except:
        break
result = list(d.values())
print(result.count(2)) # 출석한 사람 카운트