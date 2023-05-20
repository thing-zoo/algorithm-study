def solution(arr, n):
    answer = [1e9, 1e9, 1e9]
    for x in range(n-2):
        y = x + 1
        z = n - 1
        while y < z:
            total = arr[x] + arr[y] + arr[z]
            if abs(sum(answer)) > abs(total):
                answer = [arr[x], arr[y], arr[z]]
            if total > 0:
                z -= 1
            else:
                y += 1
    print(*answer)

n = int(input())
s = sorted(list(map(int, input().split())))
solution(s, n)