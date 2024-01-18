expr = input()
dic = {"+": 5, "-":5, "*": 10, "/":10, "(": 1}
op = "+-*/()"
stack = []
for e in expr:
    if e in op:
        if not stack or e == "(": # 스택이 비어있거나 '('이면 그냥 넣음
            stack.append(e)
        else:
            if e == ")": # 닫는 괄호면 여는 괄호를 만날 때 까지 pop, 출력
                while stack and stack[-1] != "(":
                    print(stack.pop(), end="")
                stack.pop() # '(' 빼기
            else:
                while stack and dic[stack[-1]] >= dic[e]: # 나보다 크거나 같은 연산자는 다 출력하기
                    print(stack.pop(), end="")
                stack.append(e)
    else: # 피연산자는 바로 출력
        print(e, end="")

while stack: # 스택에 남은 연산자 모두 출력
    print(stack.pop(), end="")