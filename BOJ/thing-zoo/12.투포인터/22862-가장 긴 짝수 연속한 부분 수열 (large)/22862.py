n, k = map(int, input().split())
s = list(map(int, input().split()))
end, count, answer = 0, 0, 0
for start in range(n): # 모든 수에 대해
    while end < n and (count < k or (count == k and s[end]%2 == 0)): # 홀수가 k개이하면서 늘릴수있을때까지
        if s[end]%2 != 0: count += 1 # 홀수를 만나면 카운트
        end += 1
    answer = max(answer, end - start - count) # 현재 길이 - 홀수 개수
    if end == n: break # 끝에 도달하면 종료
    if s[start]%2 != 0: count -=1 # 현재값이 홀수면 다시 빼주기
print(answer)