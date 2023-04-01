data = []
for i in range(5):
    n = int(input())
    data.append(n)
print(sum(data)//5)
data.sort()
print(data[2])