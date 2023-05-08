def isPrime(n): # 소수인지 확인하는 함수
    if n == 1: return False
    for i in range(2, n): # 2~n-1로 나누어지면 합성수
        if n%i == 0:
            return False
    return True
n = int(input())
data = list(map(int, input().split()))
answer = 0
for num in data:
    if isPrime(num):
        answer += 1
print(answer)