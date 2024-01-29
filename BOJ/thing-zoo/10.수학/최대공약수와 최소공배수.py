def gcd(a, b):
    if a == 0: return b
    return gcd(b%a, a)
def lcm(a, b):
    return a*b//gcd(a, b)
a, b = map(int, input().split())
print(gcd(a, b))
print(lcm(a, b))