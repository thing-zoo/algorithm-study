l, p, v = map(int, input().split())
cnt = 1
while l!=0 or p!=0 or v!=0:
    days = v//p * l
    if v%p < l:
        days+= v%p
    else:
        days += l
    print("Case ", cnt, ": ", days, sep="")
    cnt += 1

    l, p, v = map(int, input().split())
