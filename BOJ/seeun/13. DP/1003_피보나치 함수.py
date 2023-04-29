n = int(input())

fibo = [[0, 0] for _ in range(41)]
fibo[0][0] = 1
fibo[1][1] = 1
# 0, 1이 출력되는 수만 더해주면 됨
for i in range(2, 41):
    fibo[i][0] = fibo[i-1][0]+fibo[i-2][0]
    fibo[i][1] = fibo[i-1][1]+fibo[i-2][1]

for _ in range(n):
    num = int(input())
    print(*fibo[num])