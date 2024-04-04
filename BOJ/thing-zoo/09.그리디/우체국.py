# town[i]: 마을 위치, 사람수
n = int(input())
town = [list(map(int, input().split())) for _ in range(n)]
town.sort(key=lambda x: x[0]) # 마을 위치기준 오름차순 정렬
total_people = sum([town[i][1] for i in range(n)]) # 전체 사람수
count = 0 # 사람 수 카운트
for i in range(n):
    count += town[i][1]
    if count >= total_people/2: # 절반을 넘어가는 지점에
        print(town[i][0]) # 우체국 놓기
        break