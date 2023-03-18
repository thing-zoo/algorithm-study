while True:
    d = input()
    if d == ".":
        break
    stack = []
    ans = "yes"
    for i in d:
        if i == "[":
            stack.append(i)
        elif i == "]":
            if stack:
                if stack.pop() == "[":
                    continue
                else:
                    ans = "no"
                    break
            else:
                ans = "no"
                break
        elif i == "(":
            stack.append(i)
        elif i == ")":
            if stack:
                if stack.pop() == "(":
                    continue
                else:
                    ans = "no"
                    break
            else:
                ans = "no"
                break
    if stack:
        ans = "no"
    print(ans)