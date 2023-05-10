t = int(input())

for _ in range(t):
    n = int(input())
    i = 2
    cnt = 0
    while n > 1 : # n이 1이 되면 중단
        if n % i == 0: # i가 인수이면
            cnt += 1
            n //= i
        else: # 더이상 i로 나누어지지 않으면 다음 수로 넘어가기
            if cnt:
                print(i, cnt)
            cnt = 0
            i += 1
    print(i, cnt) # 마지막에 나눈 수, 횟수 출력
