import sys
input = sys.stdin.readline
n = int(input())
for i in range(1, n+1):
    cnt = 0
    height = list(map(int, input().strip().split()))
    line = [0] # 0에는 0 넣어서 제일 작은 사람을 1에 설 수 있도록
    for j in range(1, 21): # 첫번째 학생 부터 비교해나감
        length = len(line)-1
        for t in range(length, -1, -1): # 젤 뒤에서부터 키 비교
            if line[t] < height[j]: # 현재 사람이 나보다 키 작으면
                cnt += (length-t) # 뒤로 물러나야 하는 학생수
                line.insert(t+1, height[j]) # 바로 뒤에 줄 서기
                break
    print(height[0], cnt)