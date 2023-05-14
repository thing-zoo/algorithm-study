for _ in range(int(input())):
    n = int(input())
    i = 2
    prime_factor = {} # 소인수 카운트
    while i*i <= n: # 합성수의 가장 작은 약수는 n의 제곱근이하
        if n%i == 0:
            if i not in prime_factor:
                prime_factor[i] = 1
            else:
                prime_factor[i] += 1
            n //= i
        else:
            i += 1
    if n != 1:
        if n not in prime_factor:
                prime_factor[n] = 1
        else:
            prime_factor[n] += 1
    for item in sorted(prime_factor.items()): # 인수 오름차순으로
        print("%d %d" %(item[0], item[1])) # 출력
    