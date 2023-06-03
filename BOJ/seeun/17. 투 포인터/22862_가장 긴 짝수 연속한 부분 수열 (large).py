n, k = map(int, input().split())
nums = list(map(int, input().split()))

r = 0
maxlen = 0
odd = 0 # 현재 구간 안에서의 홀수의 개수
even = 0 # 현재 구간 안에서의 짝수의 개수
for l in range(n):
    while r<n and odd<=k: # r이 범위 내이고 홀수 개수가 k개 이하이면
        if nums[r] % 2 == 0:
            even += 1
        else: # 홀수이면 
            odd += 1
        r += 1

    # 처음부터 끝까지 다 세아렸으면
    if l == 0 and r == n: 
        maxlen = even
        break

    if odd == k+1:
        maxlen = max(maxlen,even)

    # 왼쪽 포인터 옮기기 전에 홀수/짝수 하나 빼주기
    if nums[l] % 2== 1:
        odd -=1
    else:
        even -=1
print(maxlen)