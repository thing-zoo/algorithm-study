def check(s):
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif i == ")" and stack[len(stack)-1] == "(":
            stack.pop()
        elif i == "(":
            stack.append(i)
    if len(stack) == 0:
        return True
    else:
        return False
        

def solution(s):
    answer = check(s)
    
    return answer