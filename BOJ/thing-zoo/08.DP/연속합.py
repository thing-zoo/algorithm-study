n = int(input())
data = list(map(int, input().split()))
current_sum = 0
max_value = -1e8
for item in data:
    current_sum = max(current_sum + item, item)
    max_value = max(max_value, current_sum)
print(max_value)