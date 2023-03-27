cnt = 0
def mul(a, b, c):
    global cnt
   
    if b==0:
        return a
    elif b == 1:
        return a %c
    
    tmp = mul(a, b//2, c)

    if b %2 == 0:
        return (tmp*tmp)%c
    else:
        return (tmp*tmp*a)%c

a, b, c = map(int, input().split())

print(mul(a, b, c))