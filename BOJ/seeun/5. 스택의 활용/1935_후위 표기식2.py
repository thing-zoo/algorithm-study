n = int(input())
string = input()
aton = {}
for i in range(n):
    aton[chr(ord('A')+i)] = int(input())
stack = []
for s in string:
    if "A" <= s <= "Z":
        stack.append(aton[s])
    else:
        op2 = stack.pop()
        op1 = stack.pop()
        if s == "*":
            stack.append(op1*op2)
        elif s== "/":
            stack.append(op1/op2)
        elif s == '+':
            stack.append(op1+op2)
        elif s == '-':
            stack.append(op1-op2)

print("%.2f" %stack[0])