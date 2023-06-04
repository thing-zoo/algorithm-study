from collections import defaultdict
for _ in range(int(input())):
    d = defaultdict(int)
    for _ in range(int(input())):
        name, type = input().split()
        d[type] += 1
    answer = 1
    for count in d.values():
        answer *= (count + 1) # 해당 종류를 착용하지 않는 경우 추가
    print(answer - 1) # 모든 종류를 착용하지 않는 경우 제외