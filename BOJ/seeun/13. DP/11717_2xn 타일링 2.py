n = int(input())
d = [0]*(n+1)

d[1] = 1

if n>=2:
    d[2] = 3
    for i in range(3, n+1):
        d[i] = d[i-1] + d[i-2]*2 #= 대신 ㅁ하나로 채우는거니까 *2 하면 됨
        d[i] %= 10007

print(d[n])