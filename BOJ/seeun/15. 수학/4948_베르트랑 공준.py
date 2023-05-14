import math

d = [1]*(2*123456+1) # 모두 소수로 가정
for i in range(2, int(math.sqrt(123456*2+1))):
    if d[i]: # i가 소수이면
        for j in range(i+i, len(d), i): # i의 배수는 소수가 아님
            d[j] = 0

n = int(input())
while n!=0:
    print(d[n+1:2*n+1].count(1))
    n = int(input())