data = list(map(int, input().split()))

max_count = 0
max_count_index = 0
for i, v in enumerate(data):
    count = data.count(v)
    if max_count < count:
        max_count = count
        max_count_index = i

if max_count == 1:
    print(max(data)*100)
elif max_count == 2:
    print(1000+data[max_count_index]*100)
else:
    print(10000+data[max_count_index]*1000)   