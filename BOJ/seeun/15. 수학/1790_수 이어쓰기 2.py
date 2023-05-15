n, k = map(int, input().split())

# 마지막으로 사용된 숫자
last_num = 0
# 현재 자릿수
num_len = 1
# 현재 자릿수의 모든 숫자의 개수
num_count = 9

while k > num_len * num_count:

    # 남은 자릿수 업데이트
    k -= num_len * num_count

    # 마지막으로 사용된 숫자
    last_num += num_count

    # 현재 자릿수 증가
    num_len += 1
    # 현재 자릿수의 모든 숫자의 개수 증가
    num_count = num_count*10
# (마지막으로 사용된 숫자 + 1) + (다음 자릿수에서 남은 숫자의 개수)
last_num = (last_num+1) + ((k-1) // num_len)

# 마지막으로 사용된 숫자가 n보다 크다면
if last_num > n:
    print(-1)
else:
    # 나머지를 계산함으로써, 마지막으로 사용된 숫자의 몇번째 숫자인지 확인
    print(str(last_num)[ (k-1) % num_len])
