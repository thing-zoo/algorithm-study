n = int(input())
divisor = sorted(list(map(int, input().split())))
if divisor == 1: print(divisor[0]*divisor[0])
else: print(divisor[0]*divisor[-1])