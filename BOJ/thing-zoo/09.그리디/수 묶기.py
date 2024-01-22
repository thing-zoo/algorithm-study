def tie(data):
    total = 0
    for i in range(0, len(data), 2):
        if i == len(data) - 1:
            total += data[i]
        elif data[i+1] == 1:
            total += data[i] + 1
        else:
            total += data[i]*data[i+1]
    return total

n = int(input())
positive, negative, zero = [], [], False
for _ in range(n):
    temp = int(input())
    if temp > 0:
        positive.append(temp)
    elif temp < 0:
        negative.append(temp)
    else:
        zero = True
positive.sort(reverse=True)
negative.sort()
if len(negative)%2 == 0:
    answer = tie(negative) + tie(positive)
else:
    answer = tie(negative[:-1]) + tie(positive)
    if not zero:
        answer += negative[-1]
print(answer)