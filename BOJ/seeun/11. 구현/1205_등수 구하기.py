import sys
input = sys.stdin.readline
n, score, p = map(int, input().rstrip().split())
if n == 0:
    print(1)
    exit()

rank = list(map(int, input().rstrip().split()))
if len(rank) == p: # 랭킹 가득 차있을 때
    if rank[-1] >= score: # 제일 낮은 점수보다 낮으면 -1 종료
        print(-1)
        exit()

ans = len(rank) # 제일 낮은 등수부터 시작
for i in range(n-1, -1, -1):
    if rank[i] <= score: # 새 점수가 더 높으면 등수를 높이면서 확인하기
        ans = i
        
if ans > p:
    print(-1)
else:
    print(ans +1)