def f(a, b, c):
    if b == 1:
        return a % c
    val = f(a, b//2, c)
    val = val * val % c # a^b*a^b=a^2b 이용
    if b % 2 == 1: val = val * a % c # b가 홀수이므로 따로 처리
    return val
    
a, b, c = map(int, input().split())
print(f(a, b, c))