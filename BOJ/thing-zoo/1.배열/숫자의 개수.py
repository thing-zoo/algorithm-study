sum = 1
for _ in range(3):
    sum *= int(input())
sum = list(map(int, str(sum)))
for i in range(10):
    print(sum.count(i))