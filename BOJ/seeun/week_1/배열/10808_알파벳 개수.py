str = input()
num = [0 for x in range(26)]

for i in str:
    num[ord(i)-97] +=1

print(*num)