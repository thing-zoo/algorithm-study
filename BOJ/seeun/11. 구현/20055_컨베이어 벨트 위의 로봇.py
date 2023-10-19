from collections import deque
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
belt = list(map(int, input().split()))
robot = [0]*n

def rotate(line):
    last = line[-1]
    for i in range(len(line)-1, 0, -1):
        line[i] = line[i-1]
    line[0] = last


step = 0
delete = 0
while belt.count(0) < k:  # 내구도0 이 k개 이상이면 종료
    step += 1
    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    rotate(belt)
    rotate(robot)
    robot[n-1] = 0


    # 2. 제일 먼저 들어간 로봇 부터 로봇 이동 시키기
    if sum(robot) > 0:
        for i in range(n-1,-1, -1):
            if robot[i] and belt[i+1]>0 and robot[i+1] == 0: # 옆칸에 내구도가 남아있으면
                robot[i] = 0
                robot[i+1] = 1 # 옆칸으로 로봇 옮기고
                belt[i+1] -= 1 # 내구도 1 감소
                robot[n-1] = 0

                # 내구도가 0이 되면 바로 종료
                if belt.count(0) >= k:
                    print(step)
                    exit()


    # 3. 로봇 하나 올리기
    if belt[0] > 0:
        belt[0] -= 1
        robot[0] = 1
        if belt.count(0) >= k:
            print(step)
            exit()
