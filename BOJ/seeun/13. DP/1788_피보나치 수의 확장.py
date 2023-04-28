n = int(input())

minus = False
if n < 0:
    minus = True
    n *= -1

if n == 0:
    print(0)
    print(0)
elif n == 1:
    print(1)
    print(1)
else:
    f1 = 0
    f2 = 1
    f = 0
    if minus:
        for i in range(2, n+1):
            f = f1 - f2
            if f<0: # 음수일때 나누기 연산하면 다르게 나오기 때문에 양수로 만들고 해야됨
                f *= -1
                f %= 1000000000
                f *= -1
            else:
                f %= 1000000000
            f1 = f2 
            f2 = f 
    else:
        for i in range(2, n+1):
            f = (f2 + f1) % 1000000000
            f1 = f2 
            f2 = f 
    if f<0:
        print(-1)
    else:
        print(1)
    print(abs(f)% 1000000000)