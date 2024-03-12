# 행복 유치원 유사문제
n = int(input()) # 센서 개수
k = int(input()) # 최대 집중국 개수
pos = list(map(int, input().split())) # 센서 위치
pos.sort() # 오름차순 정렬
diff = [pos[i+1]-pos[i] for i in range(n-1)] # 센서 간 거리차
diff.sort() # 오름차순 정렬
answer = 1e9 # 최소 집중국 간 거리 합
for i in range(1, k+1): # 모든 집중국 개수 경우에 대해
    answer = min(answer, sum(diff[:n-k])) # 거리합 구하기
print(answer)