import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    # 내코드: 완전탐색
    room = [-1]+[0]*n #0: 열림, 1: 잠김
    for i in range(2, n+1):
        for j in range(1, n+1):
            if j%i == 0:
                room[j] = not room[j]
    sys.stdout.write("%d\n" %room.count(0))

    # 다른 코드: 수학적 접근, 제곱수만 세면 되나봄
    # answer = 0 
    # for i in range(1, n):
    #     if i**2 <= n:
    #         answer += 1
    #     if i**2 > n:
    #         break
            
    # print(answer)