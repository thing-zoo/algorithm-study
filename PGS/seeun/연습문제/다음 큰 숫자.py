def solution(n):
    answer = 0
    n2 = bin(n)
    for i in range(n+1, 1000001):
        if bin(i).count('1') == n2.count('1'):
            answer = i
            break
    return answer