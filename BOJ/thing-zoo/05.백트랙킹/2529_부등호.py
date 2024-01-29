def check(a, i): # 부등호 충족하는지 확인
    flag = True
    if symbols[i-1] == '<':
        if a[i-1] >= a[i]:
            flag = False
    else:
        if a[i-1] <= a[i]:
            flag = False
    return flag


def dfs(result, x): # 결과, 마지막 인덱스
    global answer
    if len(result) > 1 and not check(result, x): # 마지막 두 숫자 부등호 확인
        return # 아니면 탈출
    if len(result) == k+1: # 전부 만족했다면
        answer.append(''.join(map(str, result))) # 문자열로 결과에 추가
        return
    for i in range(10):
        if i not in result: # 중복 불가
            dfs(result + [i], x+1)


k = int(input())
symbols = list(input().split())
answer = []
dfs([], -1) # 모든 경우의 수 확인
answer.sort() # 오름차순 정렬
print(answer[-1]) # 최대값
print(answer[0]) # 최소값