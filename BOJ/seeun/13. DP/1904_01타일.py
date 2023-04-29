n = int(input())
d = [0]*(n+1)

if n <=2:
    print(n)
else:
    d[1] = 1
    d[2] = 2
    for i in range(3, n+1):
        d[i] = (d[i-1]+d[i-2])%15746
    print(d[n]%15746)