from itertools import permutations
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
innings = []
for _ in range(n):
    innings.append(list(map(int, input().rstrip().split())))

# 행: 이닝
# 열: 선수 번호
# 1번 선수: 4번 타자로 고정 

def play(players):
    global maxScore
    # base = deque([0, 0, 0, 0])
    score = 0
    idx = 0
    for i in range(n): # 이닝 수 만큼 반복
        # base = deque([0, 0, 0, 0])
        out = 0
        b1, b2, b3 = 0, 0, 0
        while out<3:
            # i번째 이닝, 아웃이 3번 나오기 전까지 플레이어 계속 탐색
            if innings[i][players[idx]] == 0: # 아웃이면 다음으로 넘어가기
                out += 1
            elif innings[i][players[idx]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif innings[i][players[idx]] == 2:
                score += (b2 + b3) # 원래 있던 사람은 들어오고
                b1, b2, b3 = 0, 1, b1 # 새로운 사람들 두칸 이동
            elif innings[i][players[idx]] == 3:
                score += (b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 1
            elif innings[i][players[idx]] == 4:
                score += (1+b1 + b2 + b3) # 본인 포함 모든 사람 홈으로
                b1, b2, b3 = 0, 0, 0 # 초기화
            idx = (idx+1)%9
            # 덱으로 구현하면 시간초과가 뜸
            # # 1루로 이동
            # base.appendleft(1)
            # base.pop()
            # # 주자 이동
            # if base[3] == 1: # 홈에 들어왔으면
            #     score += 1
            # for _ in range(innings[i][players[idx]]-1):
            #     base.appendleft(0)
            #     base.pop()
            #     if base[3] == 1: # 홈에 들어왔으면
            #         score += 1
            # idx = (idx+1)%9
          
        maxScore = max(maxScore, score)
    return

maxScore = -1
cnt = 0
for p in permutations(range(1, 9), 8): # 1~8번 선수 중에 순열로 고름
    players = []
    players = list(p[:3]) + [0] + list(p[3:]) # 0번 선수를 4번 타자로 넣음
    play(players)
    cnt += 1
print(maxScore)