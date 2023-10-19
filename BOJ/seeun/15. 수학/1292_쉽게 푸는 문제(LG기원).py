a, b = map(int, input().split())
ans = [0 for _ in range(1001)]
idx = 1
i = 1
while i < 1001:
    for _ in range(idx): # idx를 idx번 더함
        ans[i] = ans[i-1] + idx # 누적합 계산
        i += 1
        
        if i > b:
            break
    idx += 1

print(ans[b] - ans[a-1])