n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
answer = 0 # k원을 만드는데 필요한 동전 개수의 최소값
for i in range(n-1, -1, -1): # 값이 큰 동전부터
    answer += k // a[i] # 나눠보고
    k %= a[i] # 나머지 저장
print(answer)