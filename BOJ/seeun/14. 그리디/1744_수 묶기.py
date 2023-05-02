n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()

if n == 1:
    print(nums[0])
else:
    ans = 0
    i = n-1
    while i>0:
        if nums[i-1]<0 and i%2 == 0: # 앞 숫자가 음수이고 남은 숫자가 짝수개:
            ans += nums[i] # 그냥 더하는게 이득
            i -= 1
        elif nums[i]==0 and nums[i-1]<0 and i % 2 == 1: # 현재 숫자가 0 & 앞 숫자가 음수 & 남은 음수가 홀수개:
            ans += nums[i-1] * nums[i] # 0곱해서 음수를 없애버리는 것이 이득임
            i -= 2
        elif nums[i]*nums[i-1] > nums[i]: # 곱해서 더 커지면 곱하기
            ans += nums[i-1]*nums[i]
            i -= 2
        else: # 아니면 그냥 더하기
            ans += nums[i]
            i -= 1
    if i >=0 : # 마지막 숫자 확인 못했을 경우
        ans += nums[i]
    print(ans)