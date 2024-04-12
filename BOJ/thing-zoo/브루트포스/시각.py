n, k = input().split()
n = int(n)
answer = 0
for i in range(n+1):
    for j in range(60):
        for t in range(60):
            temp = f'{i:0>2} {j:0>2} {t:0>2}'
            if k in temp:
                answer += 1
print(answer)