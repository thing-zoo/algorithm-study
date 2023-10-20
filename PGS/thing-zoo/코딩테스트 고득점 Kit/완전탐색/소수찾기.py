def isPrime(n):
    if n < 2: return False
    for i in range(2, n-1): # 1과 자신 외 나누어지면 합성수
        if n%i == 0:
            return False
    return True

def dfs(idx, numbers): # 완전탐색하면서 소수인지 확인
    global answer
    if idx:
        temp = ""
        for i in idx:
            temp += numbers[i]
        temp = int(temp)
        if temp not in result and isPrime(temp):
            answer += 1
            result.append(temp)
    
    for i in range(len(numbers)):
        if i not in idx:
            dfs(idx + [i], numbers)
            
answer = 0
result = [] # 중복 확인
def solution(numbers):
    dfs([], numbers)
    return answer