n = int(input())
if n == 1: # 1일 경우
    print(1)
    exit()

ans = 1 # 시작점 1 포함하고 시작
cnt = 1
i = 1
while cnt < n: 
    cnt += i*6 # 벌집 한바퀴 마다 칸 개수
    ans += 1
    i += 1
print(ans)