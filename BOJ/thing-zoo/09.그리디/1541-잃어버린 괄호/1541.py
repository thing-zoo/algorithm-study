exp = input().split("-")
answer = 0
result = []
for e in exp:
    arr = list(map(int, e.split("+")))
    result.append(sum(arr))
answer = result[0]
for i in range(1, len(result)):
    answer -= result[i]
print(answer)