def solution(numbers):
    answer = list(map(str, numbers))
    answer.sort(key=lambda x: x[0], reverse=True)
    return ''.join(answer)
numbers = [3, 30, 34, 5, 9]
print(solution(numbers))