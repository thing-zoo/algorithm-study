arr = list(map(int, input().split()))
def solution(arr):
    answer = []
    for i in arr:
        if answer and answer[-1] == i:
            continue
        answer.append(i)    
    return answer
print(solution(arr))