for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    answer = 0
    if dist == 0 and r1 == r2: # 같을때(접할때이기도 하므로 맨위에)
        answer = -1
    elif abs(r1 - r2) < dist < r1 + r2: # 겹칠때
        answer = 2
    elif dist == r1 + r2 or dist == abs(r1 - r2): # 접할때
        answer = 1
    print(answer)