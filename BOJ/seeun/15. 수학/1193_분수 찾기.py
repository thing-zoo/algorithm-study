n = int(input())

cnt = 0
i = 1
# n이 몇개의 연속된 숫자의 합으로 표현될 수 있는지 카운트(몇번째 대각선인지 알기 위해)
while True:
    if cnt>=n: # 임시 숫자가 n보다 커지면 멈춤
        i -=1 # n은 i-1번째 줄에 위치
        break
    else:
        cnt += i
    i+= 1

mom = 0
son = 0
if i % 2 == 0: # i가 짝수번째 대각선이면
    mom = cnt-n+1 # cnt-n: 대각선 내에서 몇번째 숫자인지
    son = i+1-mom # i번째 대각선에 있는 분모+분자는 i+1이다
else:
    son = cnt-n+1
    mom = i+1-son
print(son, "/", mom, sep="")
