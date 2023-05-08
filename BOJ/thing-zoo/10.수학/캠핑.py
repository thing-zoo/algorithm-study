i = 1
while True:
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        break
    print("Case %d: %d" %(i, v//p*l+min(v%p, l)))
    i += 1