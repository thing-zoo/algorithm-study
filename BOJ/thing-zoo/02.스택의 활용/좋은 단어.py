n = int(input())
ans = 0
for _ in range(n):
    stack = []
    data = list(input())
    for i in data:
        if stack:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    if not stack:
        ans += 1
print(ans)