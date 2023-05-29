n = int(input())

# n이하 소수 구하기
prime = []
sieve = [True]*(n+1)
sieve[0] = sieve[1] = False
for i in range(2, int(n**0.5)+1):
    if not sieve[i]: continue
    for j in range(i*i, n+1, i):
        sieve[j] = False
for i in range(n+1):
    if sieve[i]:
        prime.append(i)

# 투포인터로 연속합 구하기
answer = 0
if n > 1:
    end = 0
    total = prime[0]
    for start in range(len(prime)):
        while end < len(prime) and total < n:
            end += 1
            if end != len(prime): total += prime[end]
        if end == len(prime): break
        if total == n: answer += 1
        total -= prime[start]
print(answer)