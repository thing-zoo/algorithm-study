n = int(input())
answer = 1e9
for i in range(n//5+1): # 큰 금액인 5원부터 하나씩 나눠본다
    if (n-i*5)%2 == 0: # 나눈금액이 2로도 나눠지면
        count = i + (n-i*5)//2 # 개수를 갱신
        answer = min(answer, count)
print(answer if answer != 1e9 else -1) # 초기값 그대로면 불가능