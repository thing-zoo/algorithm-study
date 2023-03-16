def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                answer = False
    if stack:
        answer = False
    return answer

s = "(()("
print(solution(s))