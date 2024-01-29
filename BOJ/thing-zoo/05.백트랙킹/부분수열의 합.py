def f(m): # m: 배열의 인덱스
    global answer
    for i in range(m, n): # 배열의 인덱스값 m부터 n-1까지에 대해
        sub.append(data[i]) # 넣기
        if sum(sub) == s:
            answer += 1
        f(i+1) # 다음값은 다음 인덱스값부터 넣을수있음
        sub.pop() # 빼주기
n, s = map(int, input().split())
data = list(map(int, input().split()))
sub = []
answer = 0
f(0)
print(answer)