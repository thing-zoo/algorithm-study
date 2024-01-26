def find_prime(m, n):
    result = []
    prime = [True]*(n+1)
    prime[0] = prime[1] = False
    for i in range(2, n+1):
        if not prime[i]: continue
        if i >= m:
            result.append(i)
        for j in range(2*i, n+1, i):
            prime[j] = False
    return result

m = int(input())
n = int(input())
answer = find_prime(m, n)
if answer:
    print(sum(answer))
    print(min(answer))
else:
    print(-1)