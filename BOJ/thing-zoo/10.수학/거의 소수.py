def find_prime(n):
    prime = [True]*(n+1)
    prime[1] = False
    for i in range(2, n+1):
        if not prime[i]: continue
        if i*i > n: # 커지면 반복문 돌릴 필요 없으니
            break # 종료
        for j in range(i*i, n+1, i):
            prime[j] = False
    return prime

def almost_prime(a, b, end):
    count = 0
    for i in range(2, end + 1):
        if not prime_list[i]: continue
        temp = i*i
        while True:
            if temp < a:
                temp *= i
                continue
            elif temp > b:
                break
            count += 1
            temp *= i
    return count

a, b = map(int, input().split())
end = int(b ** 0.5)
prime_list = find_prime(end)
print(almost_prime(a, b, end))