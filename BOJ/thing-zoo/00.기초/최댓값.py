data = []
for _ in range(9):
    data.append(int(input()))
max = max(data)
print(max)
print(data.index(max)+1)