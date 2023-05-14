def find_prime(n): # 에라토스테네스의 체
    sieve = [False] + [True]*n
    sieve[1] = False
    for i in range(2, n+1):
        if not sieve[i]: continue
        if i*i > n: break
        for j in range(i*i, n+1, i):
            sieve[j] = False
    return sieve

prime_list = find_prime(10**6) # 범위내 소수 미리 구하기
for _ in range(int(input())):
    n = int(input())
    answer = 0
    # 골드바흐 파티션 찾기
    for i in range(2, n//2+1): # 쌍이므로 n/2까지만 보면됨
        if not prime_list[i]: continue
        if prime_list[i] and prime_list[n-i]: # 둘다 소수면
            answer += 1 # 골드바흐 파티션 카운트
    print(answer)