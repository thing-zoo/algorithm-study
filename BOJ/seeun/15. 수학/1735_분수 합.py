s1, m1 = map(int, input().split())
s2, m2 = map(int, input().split())

s3 = s1*m2 + s2*m1
m3 = m1*m2

if s3 == m3:
    s3 = 1
    m3 = 1

# 유클리드 호제법
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

div = gcd(s3, m3)
print(s3//div, m3//div)