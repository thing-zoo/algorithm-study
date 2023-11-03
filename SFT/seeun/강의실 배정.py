import sys
input = sys.stdin.readline
n = int(input())
lectures = [list(map(int, input().split())) for _ in range(n)]
lectures.sort(key=lambda x:x[1]) # 빨리 끝나는 강의 기준으로 정렬
end = lectures[0][1]
cnt = 1
for i in range(1, n):
  if end <= lectures[i][0]: # 현재 진행중인 강의 마치는 시간 이후에 수업이 시작하면 수업 가능
    end = lectures[i][1]
    cnt += 1
print(cnt)