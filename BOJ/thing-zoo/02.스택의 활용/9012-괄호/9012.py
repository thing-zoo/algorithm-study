n = int(input())
for _ in range(n):
    data = input()
    stack = []
    ans = "YES"
    for i in data:
        if i == "(":
            stack.append(i)
        else:
            if stack:
                if stack.pop() == "(":
                    continue
                else:
                    ans = "NO"
                    break
            else:
                ans = "NO"
                break
    if stack:
        ans = "NO"
    print(ans)