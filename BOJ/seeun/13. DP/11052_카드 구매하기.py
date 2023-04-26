n = int(input())
value = []
value.append(0)
value.extend(list(map(int, input().split())))

for i in range(2, n+1):
    for j in range(1,i):
        value[i] = max(value[i], value[j]+value[i-j])
print(value[n])