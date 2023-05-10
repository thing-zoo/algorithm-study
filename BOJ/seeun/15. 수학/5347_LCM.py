t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    if a == b: # 두 수가 같으면 찾을 필요가 없음
        print(a)
        continue
    i = 2
    res = 1
    while i<=min(a, b): # 두 수 중에 작은 수와 같을때 까지만 하면 됨, 어떤 수보다 커지면 약수가 아님
        if a%i == 0 and b%i==0: # i가 두 수를 나누어떨어지게 하면 공통인수임
            a //= i
            b //= i
            res *= i
        else:
            i += 1
    print(res*a*b)