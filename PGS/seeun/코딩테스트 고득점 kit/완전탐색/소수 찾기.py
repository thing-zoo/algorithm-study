from itertools import permutations
from collections import defaultdict

def isPrime(n): # 소수 판별
    if n == 1 or n == 0:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                return False
        return True

def solution(numbers):
    answer = 0
    prime = defaultdict(int)
    numbers = list(numbers)
    for i in range(1, len(numbers)+1):
        for nums in permutations(numbers, i): # numbers에서 i개를 뽑은 조합
            if isPrime(int("".join(list(nums)))):
                prime[int("".join(list(nums)))] += 1
    
    print(prime)
    answer = len(prime.keys())
    return answer

numbers = "011"	
print(solution(numbers))