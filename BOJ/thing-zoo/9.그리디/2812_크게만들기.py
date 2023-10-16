n, k = map(int, input().split())
a = list(map(int, input()))

result = []
count = 0
for i in range(n): # 앞에서 부터
    while result and a[i] > result[-1] and count < k: # 이전 수보다 a[i]가 더 크고, k가 남아있다면  
            result.pop() # 제거
            count += 1
    result.append(a[i])
while len(result) > n - k: # 현재 남은 숫자가 n-k개가 될때까지
    result.pop() # 제거
print("".join(map(str, result)))