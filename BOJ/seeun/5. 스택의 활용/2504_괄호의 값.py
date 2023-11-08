glist = list(input())
stack = []
ans = 0
tmp = 1

for i in range(len(glist)):
    if glist[i] == "(":
        stack.append(glist[i])
        tmp *= 2
    elif glist[i] == "[":
        stack.append(glist[i])
        tmp *= 3
    elif glist[i] == "]":
        if not stack or stack[-1] == "(": # 스택이 비어있거나 짝이 안맞는 상황이면 0 출력
            ans = 0
            break
        if glist[i-1] == "[": # 가장 안쪽 세트인거면 == 괄호 한 묶음이 끝났다는 말 ((['[']]))[] => 정답에 더하기
            ans += tmp
        stack.pop()
        tmp //= 3 # 끝났으니까 3 곱한거 초기화
    elif glist[i] == ")":
        if not stack or stack[-1] == "[":
            ans = 0
            break
        if glist[i-1] == "(":
            ans += tmp

        stack.pop()
        tmp //= 2

print(0 if stack else ans)
