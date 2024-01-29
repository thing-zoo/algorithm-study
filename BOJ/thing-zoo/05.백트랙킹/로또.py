def f(m):
    if len(sub) == 6: # 6개를 다 선택했으면 탈출
        print(*sub)
        return
    for i in range(m, k): #인덱스 m부터
        sub.append(s[i])  #넣기
        f(i+1) #다음값은 현재인덱스 다음값으로 접근가능
        sub.pop() #빼기

while True:
    data = list(map(int, input().split()))
    if data[0] == 0:
        break
    k, s = data[0], data[1:]
    sub = []
    f(0)
    print()