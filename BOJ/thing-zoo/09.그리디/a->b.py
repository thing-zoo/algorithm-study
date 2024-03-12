a, b = map(int, input().split())
answer = 0 # 필요한 연산 최솟값
flag = False # 변환 가능 여부
while b > 0:
    if b%2 == 0: # 2로 나눠지면
        b //= 2 # 2로 나누기
    elif b%10 == 1: # 일의자리가 1이면
        b //= 10 # 제거
    else: # 나머지는
        break # 불가능한 경우
    answer += 1 # 연산 횟수 카운트
    if a == b: # 같아지면
        flag = True # 변환 가능
        break # 종료
print(answer+1 if flag else -1)