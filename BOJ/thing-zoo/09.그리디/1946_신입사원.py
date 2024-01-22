import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    rank = [tuple(map(int, input().rstrip().split())) for _ in range(n)]
    rank.sort() # 서류성적 기준 오름차순 정렬
    answer = 1 # 최종 선발 인원(rank[0]은 서류 1등이므로 선발됨)
    min_value = rank[0][1] # 이전 지원자들중 가장 높은 면접 성적
    for i in range(1, n): # 남은 인원에 대해
        if min_value > rank[i][1]: # 면접 성적이 이전 지원자들중 가장 높은 성적보다 높다면
            answer += 1 # 선발
            min_value = rank[i][1] # 갱신
    print(answer)