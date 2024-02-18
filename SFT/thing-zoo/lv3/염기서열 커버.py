import sys

# 두 초염기서열 합치기
def merge(dna1, dna2):
    if dna1 == [] or dna2 == []: # 해당하는 초염기서열이 없다면
        return [] # 합칠수없음
    dna = []
    for i in range(M):
        if dna1[i] == '.':
            dna.append(dna2[i])
        elif dna2[i] == '.':
            dna.append(dna1[i])
        elif dna1[i] == dna2[i]:
            dna.append(dna1[i])
        else:
            return [] # 합칠수없음
    return dna

# index에 대한 초염기서열 구하기
def genSuperDNA(index):
    '''
    EX) index = 1010
    loc = 1
    0010 = 2**loc
    1000 = index - 2**loc
    '''
    loc = 0 # 가장 오른쪽 1의 인덱스
    tempIndex = index
    while tempIndex % 2 == 0:
        tempIndex //= 2
        loc += 1
    superDNA[index] = merge(dna[loc], superDNA[index - 2**loc])

# 해당 경우의 수(index)를 커버하기 위한 초염기서열의 최소 개수 구하기(DP)
def getAnswer(index):
    if answer[index] < N+1: # 이미 구했다면
        return answer[index] # 반환

    bit1 = [] # 비트가 1인 인덱스들
    number1 = number2 = 0
    tempIndex = index
    
    for i in range(N):
        if tempIndex % 2 == 1:
            bit1.append(i)
            number2 += 2**i
        tempIndex //= 2

    digit = [0] * len(bit1)

    # 경우의 수(index)에 대한 경우의수를 모두 구해서 최소 염기서열 개수 구하기
    for i in range(1, 2 ** (len(bit1)-1)): # 대칭이라 절반만해도 원하는 결과가 나옴
        for j in range(len(bit1)):
            temp = 2 ** bit1[j]
            if digit[j] == 1:
                digit[j] = 0
                number1 -= temp
                number2 += temp
            else:
                digit[j] = 1
                number1 += temp
                number2 -= temp
                break
        answer[index] = min(answer[index], getAnswer(number1) + getAnswer(number2))
    return answer[index]


N, M = map(int, sys.stdin.readline().rstrip().split())
dna = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

# superDNA[i]=경우의수 i에 대한 초염기서열
# 염기서열이 N개이므로 경우의 수 2^N
superDNA = [None for _ in range(2**N)]
superDNA[0] = ['.'] * M

# answer[i]=경우의수 i를 커버하기 위한 초염기서열의 최소 개수
# 염기서열은 N개이므로 무한대개념으로 N+1 초기화
answer = [N+1 for _ in range(2**N)]
answer[0] = 0

# 모든 경우에 따른 초염기서열 구하기
for i in range(1, 2**N): # 0001(1) ~ 1111(2^N-1)
    genSuperDNA(i)

# 모든 경우에 필요한 최소 염기서열 개수 구하기
for i in range(1, 2**N):
    if superDNA[i]: # 초염기서열이 있으므로
        answer[i] = 1 # 1개
    else: # 없으면
        getAnswer(i) # 구하기

print(answer[2**N-1])