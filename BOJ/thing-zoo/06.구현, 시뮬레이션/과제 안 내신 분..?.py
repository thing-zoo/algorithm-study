students = [False]*31
for _ in range(28):
    n = int(input())
    students[n] = True
answer = [i for i in range(1, 31) if not students[i]]
answer.sort()
for i in answer:
    print(i)