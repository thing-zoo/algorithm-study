data = input()
ans = 0
stack = []
for i in range(len(data)):
    if data[i] == "(":
        stack.append(data[i])
    else: # )
        if stack[-1] == "(":
            stack.pop()
            if data[i-1] == ")":
                ans += 1
            else:
                ans += len(stack)
print(ans)