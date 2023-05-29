n = int(input())
nums = [1] * (n+1)
nums[1] = 0
for i in range(2, n+1):
    if nums[i] == 1:
        for j in range(i+i, n+1, i):
            nums[j] = 0

prime = []
# 소수만 담는 배열
for i in range(2, n+1):
    if nums[i]:
        prime.append(i)

total = 0
cnt = 0
j = 0
for i in range(len(prime)):
    while j<len(prime) and total<n: # 합이 n미만이고 j가 범위 내에 있으면
        total += prime[j] # 소수 더해주기
        j += 1 # 한칸 옆으로 이동

    if total == n: # 합이 n이면 cnt++
        cnt += 1

    total -= prime[i] # 왼쪽 포인터를 옮길 거기 때문에 total에서 i값 빼주기
print(cnt)