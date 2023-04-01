def hanoi(a, b, n):
    if n == 1:
        return result.append([a, b])
    hanoi(a, 6-b-a, n-1)
    result.append([a, b])
    hanoi(6-b-a, b, n-1)
n = int(input())
result = []
hanoi(1, 3, n)
print(len(result))
for i in range(len(result)):
    print(*result[i], sep=" ")