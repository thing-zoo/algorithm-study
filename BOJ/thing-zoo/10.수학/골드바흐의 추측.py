def find_prime(n): # 에라토스테네스의 체
    sieve = [False] + [True]*n
    sieve[1] = False
    for i in range(2, n+1):
        if not sieve[i]: continue
        if i*i > n: break
        for j in range(i*i, n+1, i):
            sieve[j] = False
    return sieve

prime_number = find_prime(10**4)
for _ in range(int(input())):
    n = int(input())
    gold_bach = []
    for i in range(2, n//2 + 1):
        if prime_number[i] and prime_number[n-i]:
            gold_bach.append([i, n-i])
    gold_bach.sort(key=lambda x: x[1]-x[0])
    print(gold_bach[0][0], gold_bach[0][1])