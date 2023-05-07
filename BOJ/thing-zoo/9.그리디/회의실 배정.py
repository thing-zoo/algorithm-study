n = int(input())
meeting = [list(map(int, input().split())) for _ in range(n)]
meeting.sort(key=lambda x: (x[1], x[0])) # 끝나는 시간, 시작시간이 빠른순으로 정렬
t = 0; answer = 0
for i in range(n):
    if t > meeting[i][0]: # 현재시간보다 시작시간이 빠르면
        continue # 넘기기
    answer += 1 # 끝나는 시간이 가장 빠른것이 선택됨
    t = meeting[i][1] # 현재시간을 끝나는 시간으로
print(answer)