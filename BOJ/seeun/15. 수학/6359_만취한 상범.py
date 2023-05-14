t = int(input())
for _ in range(t):
    n = int(input())
    prison = [True] * (n+1) #False: 닫힌 , True: 열린
    prison[0] = False
    for i in range(2, n+1):
        for j in range(i, n+1, i): # i의 배수 방 닫기/열기
            prison[j] = not prison[j]
    print(prison.count(True))