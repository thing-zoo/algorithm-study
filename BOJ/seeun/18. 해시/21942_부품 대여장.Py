from collections import defaultdict
import re, sys
input = sys.stdin.readline
n, l, f = map(str, input().rstrip().split())
n, f = int(n), int(f) # 숫자로 변환
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
l = list(map(int, re.split(r"/|:", l))) # 대여기간 split
l = l[2] + l[1]*60 + l[0] * 60 * 24 # 대여기간 분으로 변환

borrow = {} # 대여 명부
ans = defaultdict(int) # 벌금 내야하는 사람, 금액 체크
for _ in range(n):
    info = input().rstrip().split()
    date = list(map(int, info[0].split('-'))) # 날짜 '-'로 분리
    time = list(map(int, info[1].split(':'))) # 시간 ':'로 분리
    object = info[2] # 대여한 물품
    name = info[3].strip() # 대여한 사람
    
    # 대여/반납 시각 분으로 변경
    t = time[1] + time[0]*60 # 분+시
    t += (date[2]-1) * 24 * 60 # 일
    t += 24 * 60 * sum(days[:date[1]]) # 월: 1~현재 월까지 "누적합" 한 날짜만큼

    if (name, object) not in borrow or borrow[(name, object)] == -1: # 처음 대여 or 반납된 물품 다시 빌리는 경우
        borrow[(name, object)] = t # 대여 시각 저장
    else: # 반납하는 경우
        if borrow[(name, object)] + l < t: # 반납해야하는 시각 < 반납 시각 이면 벌금 내야함
            ans[name] += (t-(borrow[(name, object)] + l)) * f # 늦은 만큼 벌금
        borrow[(name, object)] = -1 # 반납 표시
            
if ans:
    ans = list(ans.items())
    ans.sort() # 사전순으로 정렬 후 출력
    for a in ans:
        print(a[0], a[1])
else:
    print(-1)