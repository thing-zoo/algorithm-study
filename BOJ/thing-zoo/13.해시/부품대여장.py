from datetime import datetime, timedelta
from collections import defaultdict
import sys
input = sys.stdin.readline
def init():
    n, l, f = input().rstrip().split()
    term = timedelta(days=int(l[:3]), hours=int(l[4:6]), minutes=int(l[7:]))
    return int(n), term, int(f)

borrow = defaultdict(dict)
answer = defaultdict(int)
N, term, F = init()
for _ in range(N):
    *t, P, M = input().rstrip().split()
    now = datetime.strptime(' '.join(t), '%Y-%m-%d %H:%M')
    if P in borrow[M]:
        if borrow[M][P] + term < now: # 대여기간 넘기면
            gap = (now - borrow[M][P] - term)//timedelta(minutes=1) # 초과분
            answer[M] += gap*F # 벌금
        del borrow[M][P] # 반납
    else:
        borrow[M][P] = now # 대여일

if not answer:
    print(-1)
else:
    for k in sorted(answer.keys()):
        print(k, answer[k])