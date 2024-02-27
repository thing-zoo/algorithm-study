n = int(input())
tips = [int(input()) for _ in range(n)]
tips.sort(reverse=True) # 내림차순 정렬
answer = 0 # 팁의 최댓값
for i in range(n):
    tip = tips[i]-(i+1-1) # 팁=기존팁-(등수-1)
    if tip > 0: # 양수만 가능
        answer += tip
print(answer)