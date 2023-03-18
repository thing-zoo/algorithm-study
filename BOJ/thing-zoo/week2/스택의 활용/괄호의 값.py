data = input()
stack = []
ans = 0
tmp = 1
for i in range(len(data)):
    if data[i] == "(":
        stack.append(data[i])
        tmp *= 2
    elif data[i] == "[":
        stack.append(data[i])
        tmp *= 3
    elif data[i] == ")":
        if stack and stack[-1] == "(":
            stack.pop()
            if data[i-1] == "(":
                ans += tmp
            tmp //=2
        else:
            ans = 0
            break
    elif data[i] == "]":
        if stack and stack[-1] == "[":
            stack.pop()
            if data[i-1] == "[":
                ans += tmp
            tmp //=3
        else:
            ans = 0
            break
if stack:
    ans = 0
print(ans)