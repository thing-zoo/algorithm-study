for _ in range(int(input())):
    n, m = map(int, input().split())
    answer = 1
    for i in range(1, m+1): answer *= i
    for i in range(1, n+1): answer //= i
    for i in range(1, m-n+1): answer //= i
    print(answer)