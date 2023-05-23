import bisect
# 모든 부배열의 합 구하는 함수
def find_sum_of_intervals(arr, n):
    # dp[i]: i까지의 합
    dp = [0]*n
    dp[0] = arr[0]
    for i in range(1,n):
        dp[i] = dp[i-1] + arr[i]
    # 구간합(i, j) = dp[j] - dp[i-1]
    sum_of_intervals = []
    for i in range(n):
        sum_of_intervals.append(dp[i])
        for j in range(i):
            sum_of_intervals.append(dp[i]-dp[j])
    return sorted(sum_of_intervals)

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

sum_of_intervals_a = find_sum_of_intervals(a, n)
sum_of_intervals_b = find_sum_of_intervals(b, m)

answer = 0
for x in sum_of_intervals_a:
    lower = bisect.bisect_left(sum_of_intervals_b, t - x)
    upper = bisect.bisect_right(sum_of_intervals_b, t - x)
    answer += upper - lower # 쌍의 개수 카운트
print(answer)