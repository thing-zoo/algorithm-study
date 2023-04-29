N = int(input())

d = [[0]*10 for _ in range(N+1)]
for i in range(1, 10):
    d[1][i] = 1

MOD = 1000000000

for i in range(2, N+1):
    for j in range(10):
        if j == 0: # 0으로 시작하면 1밖에 못옴, 0으로 시작하는 숫자는 세아리지 않음
            d[i][j] = d[i-1][1]
        elif j == 9: # 9 뒤에는 8밖에 못오기 때문에 8로 시작하는것의 개수 사용 하면 됨
            d[i][j] = d[i-1][8]
        else:
            d[i][j] = d[i-1][j-1]+d[i-1][j+1] # j뒤에 올 수 있는 수는 j-1, j+1 두개 이기 때문에 그 값 이용 가능
print(sum(d[N]) % MOD)