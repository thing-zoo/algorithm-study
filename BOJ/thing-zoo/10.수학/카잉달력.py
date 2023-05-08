def gcd(a, b): # 최대공약수
    if a == 0: return b
    return gcd(b%a, a)
def lcm(a, b): # 최대공배수
    return a * b // gcd(a, b)
def f(m, n, x, y):
    if x == m: x = 0
    if y == n: y = 0
    l = lcm(m, n)
    for i in range(x, l+1, m): # x에서 m씩 더해 최소공배수까지
        if i == 0: continue
        if i%n == y: # 그수가 n으로 나눴을때 y면
            return i
    return -1

t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    print(f(m,n,x,y))