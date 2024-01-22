import sys
from itertools import permutations
input = sys.stdin.readline
# def play(order): # 야구 경기를 진행하는 함수
#     score = 0
#     j = 0 # 선수 순서
#     for i in range(n): # i번째 이닝
#         bases = [False]*4 # 홈 1루 2루 3루
#         out = 0
#         while out < 3: # 3아웃시 종료
#             result = data[i][order[j]] # 결과값
#             bases[0] = True # 출발
#             if result == 0: # 아웃
#                 out += 1
#             else:
#                 for k in range(3, -1, -1):
#                     if not bases[k]: # 선수가없음
#                         continue
#                     if k + result > 3: # 홈런
#                         score += 1
#                     else: # 결과값만큼 이동
#                         bases[k + result] = True
#                     bases[k] = False # 원래자리는 비우기
#             j = (j + 1)%9 # 다음 타자
#     return score
def play(order): # 깐깐한 백준에서는 이렇게 풀어야함..
    score = 0
    j = 0 # 선수 순서
    for i in range(n): # i번째 이닝
        b1, b2, b3 = 0, 0, 0
        out = 0
        while out < 3: # 3아웃시 종료
            if data[i][order[j]] == 0: # 아웃
                out += 1
            elif data[i][order[j]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif data[i][order[j]] == 2:
                score += (b2 + b3)
                b1, b2, b3 = 0, 1, b1
            elif data[i][order[j]] == 3:
                score += (b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 1
            else:
                score += (1 + b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 0
            j = (j + 1)%9 # 다음 타자
    return score

n = int(input())
data = [list(map(int, input().rstrip().split())) for _ in range(n)]
answer = 0
for selected in permutations(range(1, 9), 8): # 타순 정하기
    selected = list(selected)
    order = selected[:3] + [0] + selected[3:] # 4번째는 무조건 1번타자로
    answer = max(play(order), answer) # 경기 진행
print(answer)