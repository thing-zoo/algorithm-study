n = int(input())
count = 0
for i in range(666, 10**9):
    if '666' in str(i):
        count += 1
        if count == n:
            print(i)
            break