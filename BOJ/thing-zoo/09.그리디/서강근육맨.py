n = int(input())
t = list(map(int, input().split()))
t.sort(reverse=True) # 내림차순 정렬
if n%2 != 0: # 홀수인 경우 짝수처럼 만들기
    t += [0]
    n += 1
answer = 0
for i in range(n//2): # 최소가 되도록
    answer = max(answer, t[i]+t[n-1-i]) # 두값 더하기
print(answer)