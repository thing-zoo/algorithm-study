n, m = map(int, input().split())
monster = {}
num = {}
for i in range(1, n+1):
    tmp = input()
    num[i] = tmp
    monster[tmp] = i

for i in range(m):
    tmp = input()
    if tmp.isalpha():
        print(monster[tmp])
    else:
        print(num[int(tmp)])