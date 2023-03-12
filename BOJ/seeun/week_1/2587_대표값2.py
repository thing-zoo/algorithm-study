n = []
for i in range(5):
    n.append(int(input()))

n.sort()
print(sum(n)//5)
print(n[2])