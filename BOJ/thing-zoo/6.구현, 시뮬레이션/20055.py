from collections import deque
n, k = map(int, input().split())
data = list(map(int, input().split()))
belt = deque([[data[i], False] for i in range(2*n)]) # 내구도, 로봇 여부
level = 1 # 단계 수행 횟수
count = 0 # 0의 개수 세기
while True:
    # 벨트 회전하기
    if belt[n-1][1]: # 내리는 위치에 로봇이 있으면
        belt[n-1][1] = False # 내리기
    belt.rotate(1) # 뒤에서 하나 가져오기

    for i in range(n-1, -1, -1): # 뒤에서부터
        if i == n-1 and belt[i][1]: # 내리는 곳이고 로봇이 있으면
            belt[n-1][1] = False  # 내리기
        else:
            if belt[i][1] and not belt[i+1][1] and belt[i+1][0] >= 1: # 로봇이 있고 다음칸에 로봇이 없고 내구도 1이상이면
                belt[i][1] = False
                belt[i+1][1] = True # 로봇 이동
                belt[i+1][0] -= 1 # 내구도 감소
                if belt[i+1][0] == 0: # 내구도 0이면
                    count += 1 # 카운트

    # 로봇 올리기
    if belt[0][0] != 0: # 내구도가 0이 아니면
        belt[0][0] -= 1 # 내구도 감소
        belt[0][1] = True # 올리기
        if belt[0][0] == 0:  # 내구도 0이면
            count += 1  # 카운트

    if count >= k: # 내구도 0 개수가 k개 이상이면 
        break # 종료
    level += 1 # 단계 증가
print(level)