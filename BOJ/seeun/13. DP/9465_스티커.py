import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    num = int(input())
    sticker = []
    sticker.append(list(map(int, input().rstrip().split())))
    sticker.append(list(map(int, input().rstrip().split())))
    if num == 1:
        print(max(sticker[0][0], sticker[1][0]))
    else:
        d = [[0]*num for _ in range(2)]
        d[0][0] = sticker[0][0]
        d[1][0] = sticker[1][0]
        d[0][1] = max(d[0][0], d[1][0]+sticker[0][1])
        d[1][1] = max(d[1][0], d[0][0]+sticker[1][1])
        # 바로전칸의 다른층 vs 전전칸의 두층 - 세개 중에 큰것
        for i in range(2, num):
            d[0][i] = max(d[0][i-2], d[1][i-2], d[1][i-1]) + sticker[0][i]
            d[1][i] = max(d[0][i-2], d[1][i-2], d[0][i-1]) + sticker[1][i]
        print(max(d[1][num-1], d[0][num-1]))