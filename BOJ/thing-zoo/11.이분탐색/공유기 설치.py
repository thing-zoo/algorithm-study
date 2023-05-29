import sys
input = sys.stdin.readline # 21퍼 실패 원인
n, c = map(int, input().rstrip().split())
pos = sorted([int(input()) for _ in range(n)])
answer = 0 # 최대 거리

start = 1
end = pos[-1] - pos[0] # 가능한 최대 거리
while start <= end:
    mid = (start + end)//2

    # 현재 거리로 놓을 수 있는 공유기 수 구하기
    now, count = 0, 1
    for i in range(1, n):
        if pos[now] + mid <= pos[i]:
            now = i
            count += 1
    
    if count >= c: # c개이상이면
        answer = max(answer, mid) # 정답 갱신
        start = mid + 1
    else: end = mid - 1
print(answer)