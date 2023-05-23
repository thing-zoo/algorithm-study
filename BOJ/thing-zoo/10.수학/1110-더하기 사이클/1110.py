n = int(input())
answer = 0
pre = n
new = -1
while new != n:
    new = pre%10*10 + (pre//10 + pre%10)%10
    pre = new
    answer += 1
print(answer)