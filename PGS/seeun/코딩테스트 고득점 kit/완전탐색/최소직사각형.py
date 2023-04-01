sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]

def solution(sizes):
    answer = 0
    width = -1
    length = -1
    for i in range(len(sizes)):
        a, b = sizes[i][0], sizes[i][1]
        if a > b: # 둘 중에 작은 값을 a에 담음
            tmp = a
            a = b
            b = tmp
        # max 값 찾는 과정 (모든 명함이 들어가려면 최대값으로 길이 정해야함)    
        if width<a:
            width = a
        if length<b:
            length = b

    answer = length*width
    print(answer)
    return answer
    
solution(sizes)