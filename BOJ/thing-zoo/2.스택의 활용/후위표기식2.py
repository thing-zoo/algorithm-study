n = int(input())
exp = input()
data = [int(input()) for _ in range(n)]
stack = []
for e in exp:
    if e.isalpha():
        stack.append(data[ord(e)-ord('A')])
    else:
        y = stack.pop()
        x = stack.pop()
        if e == '+':
            x += y
        elif e == '-':
            x -= y
        elif e == '*':
            x *= y
        else:
            x /= y
        stack.append(x)
print(f'{stack[0]:.2f}')