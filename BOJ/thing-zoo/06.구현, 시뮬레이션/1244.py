def change(x):
    if swiches[x] == 1: swiches[x] = 0
    else: swiches[x] = 1

n = int(input()) # 스위치 개수
swiches = [-1] + list(map(int, input().split())) # 스위치
m = int(input()) # 학생수
for _ in range(m):
    gender, x = map(int, input().split())
    if gender == 1: # 남학생
        for i in range(1, n+1):
            if i%x == 0: # x의 배수이면
                change(i)
    else: # 여학생
        change(x)
        for i in range(1, n//2):
            if x-i < 1 or x+i > n: # 인덱스 밖이면
                break # 탈출
            if swiches[x-i] == swiches[x+i]: # 대칭이면
                change(x-i)
                change(x+i)
            else: # 대칭이 아니면
                break # 탈출
for i in range(1, n+1):
    print(swiches[i], end=' ')
    if i%20 == 0: print()