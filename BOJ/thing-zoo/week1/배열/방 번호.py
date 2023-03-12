n = list(map(int, input()))
count = []

#각 수들의 카운트를 세서 최댓값만큼 세트 필요
for i in range(10):
    count.append(n.count(i))

sum = count[6]+ count[9]
count[6] = sum//2
count[9] = sum - count[6]

print(max(count))