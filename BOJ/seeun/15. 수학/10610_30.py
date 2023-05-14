n = list(input())
n.sort(reverse=True)
n = list(map(int, n))
if sum(n)%3==0:
    tmp = int("".join(list(map(str, n))))
    if tmp%10 == 0:
        print(int("".join(list(map(str, n)))))
    else:
        print(-1)
else:
    print(-1)