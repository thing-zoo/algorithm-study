a, b = map(int, input().split())
# a, b 사이에 있는 소수의 제곱수 찾기
# 배열에 소수인 애들 표시
# a 보다 큰소수인애 b보다 작게 몇번 제곱할 수 있는지 세아리기
# *** 제곱수가 범위 내에 있는지 확인하는것이기 때문에 b의 제곱근까지의 소수만 구하면 됨. 그 이상은 어차피 n제곱하면 b보다 커짐
nums = [1]*(int(b**0.5)+1) 


nums[1] = 0
for i in range(2, int(b**0.5)+1):
    if nums[i] == 1: # 이 조건문이 있어야 시간초과가 안남
        if i*i>int(b**0.5):
            break
        for j in range(i*i, int(b**0.5)+1, i): # 소수의 배수 지워주기
            nums[j] = 0

cnt = 0
for i in range(1, len(nums)):
    if nums[i] == 1: #i가 소수이면
        tmp = i*i #제곱수부터 확인
        while True: # 제곱수가 범위 내에 있으면
            if tmp>b:
                break
            if tmp<a:
                tmp *= i
                continue
            cnt += 1
            tmp *= i
print(cnt)