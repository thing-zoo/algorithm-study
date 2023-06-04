n = int(input())
answer = 1e9
for i in range(n):
    total, m = i, i # 분해합, m
    while m: # m이 0이 될때까지
        total += m%10 # 자릿수 더하기
        m //= 10 # 더한 자릿수 제거
    if total == n: # m의 분해합이 n이면
        answer = min(answer, i) # 정답 갱신
print(answer if answer != 1e9 else 0) # 불가능하면 0