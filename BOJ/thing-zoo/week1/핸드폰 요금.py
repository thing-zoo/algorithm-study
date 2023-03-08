def cost(x, t):
    #x: 요금제, t:시간
    cost = 0
    if x == 1:
        cost += t//30*10 + 10
    else:
        cost += t//60*15 + 15
    return cost

n = int(input())
time = list(map(int, input().split()))
a = b = 0
for i in time:
    a += cost(1, i)
    b += cost(2, i)

if a < b:
    print('Y', end=" ")
    print(a)
elif a == b:
    print('Y', end=" ")
    print('M', end=" ")
    print(b)
else:
    print('M', end=" ")
    print(b)