n = int(input())
ring = list(map(int, input().split()))

# 유클리드 호제법
def gcd(a, b):
    while b>0:
        a, b = b,  a%b
    return a

for i in range(1, n):
    gcdnum = gcd(ring[0], ring[i])
    print(ring[0]//gcdnum, "/", ring[i]//gcdnum, sep="")
    