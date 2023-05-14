n = int(input())
i = 2
while i*i <= n: # 합성수의 가장 작은 약수는 루트n 이하
    if n%i == 0:
        print(i)
        n //= i
    else:
        i += 1
if n != 1:
    print(n)