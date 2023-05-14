n, k = map(int, input().split())
prime = [True]*(n+1)
prime[1] = False
count = 0
for i in range(2, n+1): # 2부터 n까지
    if not prime[i]: # 지웠다면
        continue # 넘어가기
    count += 1 # P 지우기
    if count == k:
        print(i)
        break
    for j in range(i*i, n+1, i): # i의 배수 
        if not prime[j]: # 지웠다면
            continue # 넘어가기
        prime[j] = False # 지우기
        count += 1
        if count == k:
            print(j)
            exit(0)