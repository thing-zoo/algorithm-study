def solution(numbers, hand):
    answer = ''
    left = [1, 4, 7] # 무조건 왼손으로 누를 숫자
    right = [3, 6, 9] # 무조건 오른손으로 누를 숫자
    location = {}
    n = 1
    
    # 1~# 까지의 위치 정보 저장
    for i in range(4):
        for j in range(3):
            if n == 10:
                location['*'] = [i, j]
            elif n == 11:
                location[0] = [i, j]
            elif n == 12:
                location['#'] = [i, j]
            else:
                location[n] = [i, j]
            n += 1
            
    # 키패드 누르기 시작  
    lhand = location['*'] # 초기 왼손 위치
    rhand = location["#"] # 초기 오른손 위치
    
    for n in numbers:
        if n in left:
            answer += "L"
            lhand = location[n]
        elif n in right:
            answer += "R"
            rhand = location[n]
        else: # 2, 5, 8, 0 이면 둘중에 가까운 손으로
            x, y = location[n]
            if abs(x-lhand[0]) + abs(y-lhand[1]) < abs(x-rhand[0]) + abs(y-rhand[1]):
                answer += 'L'
                lhand = location[n]
            elif abs(x-lhand[0]) + abs(y-lhand[1]) > abs(x-rhand[0]) + abs(y-rhand[1]):
                answer += 'R'
                rhand = location[n]
            else: # 두 손의 거리가 같다면 어느 손잡이인지에 따라
                if hand == "right":
                    answer += 'R'
                    rhand = location[n]
                else:
                    answer += 'L'
                    lhand = location[n]
          
    return answer