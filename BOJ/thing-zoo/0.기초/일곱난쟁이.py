data = []
for i in range(9):
    data.append(int(input()))

error = sum(data) - 100
end = False
for i in range(9):
    a = data[i]
    for j in range(i+1, 9):
        b = data[j]
        if a + b == error:
            data.remove(a)
            data.remove(b)
            end = True
            break
    if(end):
        break

for i in sorted(data):
    print(i)