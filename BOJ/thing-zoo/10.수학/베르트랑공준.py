# 테스트케이스 입력받기
data = []
while True:
    temp = int(input())
    if temp == 0:
        break
    data.append(temp)

# 에라토스테네스의 체로 소수 찾기
n = 2*max(data)
prime = [True]*(n+1)
prime[1] = False
for i in range(2, n+1):
    if not prime[i]:
        continue
    for j in range(i*i, n+1, i):
        prime[j] = False

# 소수 개수 구하기
count = [0]*(n+1)
for i in range(2, n+1):
    if prime[i]:
        count[i] = count[i-1] + 1
    else:
        count[i] = count[i-1]

# n < P <= 2*n인 소수 개수 출력
for i in data:
    print(count[i*2]-count[i])