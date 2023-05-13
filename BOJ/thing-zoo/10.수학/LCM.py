def gcd(a, b): # 최대공약수 함수
    if a == 0: return b
    return gcd(b%a, a)
def lcm(a, b): # 최소공배수 함수
    return a*b//gcd(a, b)

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(lcm(a, b))