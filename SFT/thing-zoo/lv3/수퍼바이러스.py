k, p, n = map(int, input().split())
# pow 함수 사용
# print(k*pow(p, 10*n, 1000000007)%1000000007)

# 재귀 사용
def f(a, b):
    if b == 1:
        return a
    elif b % 2 == 0:
        c = f(a, b//2)
        return c*c%1000000007
    else:
        c = f(a, (b-1)//2)
        return c*c*a%1000000007
    
k, p, n = map(int, input().split())
print(k*f(p, 10*n)%1000000007)