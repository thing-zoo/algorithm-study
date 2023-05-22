n = int(input())
if n%5 == 0: # 5의 배수면
    answer = n//5 # 몫
else:
    answer = 1e9
    for i in range(n//5, -1, -1): # 몫에서 1씩 줄여가며
        if (n - i*5)%3 == 0: # 나머지가 3의 배수인지 확인
            answer = min(answer, i + (n - i*5)//3) # 최소값 찾기
    if answer == 1e9: # 답이 없는 경우
        answer = -1
print(answer)