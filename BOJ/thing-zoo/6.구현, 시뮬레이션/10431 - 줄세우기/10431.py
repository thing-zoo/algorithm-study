import bisect
for _ in range(int(input())):
    data = list(map(int, input().split()))
    line = [data[1]]
    count = 0
    for x in data[2:]:
        pos = bisect.bisect_left(line, x) # 삽입할 가장 왼쪽 인덱스 반환
        if pos != len(line): # 맨 마지막이 아니면
            count += len(line) - pos # 걸음 수 세기
        line.insert(pos, x)
    print(data[0], count, sep=' ')