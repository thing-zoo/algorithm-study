for _ in range(int(input())):
    h, w, n = map(int, input().split())
    level = n%h
    room = n//h+1
    if level == 0: # n이 h의 배수인 경우는 예외
        level = h
        room = n//h
    print(level*100+room)