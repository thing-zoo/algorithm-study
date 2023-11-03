n, k = map(int, input().split())
line = list(input())
answer = 0
for i in range(n):
    if line[i] == 'P':
        for j in range(i-k, i+k+1):
            if j < 0 or j >= n: continue
            if line[j] == 'H':
                line[j] = '-'
                answer += 1
                break
print(answer)