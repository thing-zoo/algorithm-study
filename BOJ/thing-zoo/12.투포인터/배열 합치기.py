import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = list(map(int, input().rstrip().split()))
B = list(map(int, input().rstrip().split()))
C = []

a = 0
b = 0
# 두 배열의 현재 최소값 비교해서 C에 넣고
while a != n and b != m:
    if A[a] < B[b]:
        C.append(A[a])
        a += 1
    else:
        C.append(B[b])
        b += 1
        
# 남은건 비교할 필요없으니 그냥 뒤에 붙이기
if a < n:
    C += A[a:]
elif b < m:
    C += B[b:]
print(' '.join(map(str, C)))