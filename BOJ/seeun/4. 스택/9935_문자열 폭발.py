S = input()
bomb = input()
stack = []

for s in S:
    stack.append(s) # 일단 스택에 넣고
    if "".join(stack[-len(bomb):]) == bomb: # 마지막에 bomb와 같은 문자열이 있으면 해당 문자열 pop
        for _ in range(len(bomb)):
            stack.pop()

print("".join(stack) if len(stack) > 0 else "FRULA")