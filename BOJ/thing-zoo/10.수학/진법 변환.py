n, b = input().split()
n = n[::-1]
b = int(b)
answer = 0
for i in range(len(n)):
    if n[i].isalpha():
        x = ord(n[i])-ord('A')+10
    else:
        x = int(n[i])
    answer += pow(b, i)*x
print(answer)