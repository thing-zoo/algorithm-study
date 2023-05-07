n = int(input())
w = [int(input()) for _ in range(n)]
w.sort() # 오름차순으로 정렬
answer = 0 # 로프로 들어올릴수있는 최대중량
for k in range(1, n+1): # 로프 k개 선택
    answer = max(answer, w[-k]*k) # k개중에서 최소값의 k배만큼이 최대중량
print(answer)