n = int(input())
nums = list(map(int, input().split()))
nums.sort()
cnt = 0
for i in range(n-2):
    if nums[i] > 0: # 이게 0보다 크면 뒤에 숫자들은 다 보다 크기 때문에 합해서 0을 만들 수 없음
        break
    s = i+1
    e = n-1
    while s<e:
        if sum([nums[i], nums[s], nums[e]]) == 0:
            if nums[s] == nums[e]: # 두 숫자가 같음 == 사이에 있는 숫자가 모두 같다는 말
                cnt += (e-s+1)*(e-s)//2
                break
            else: # 두 숫자가 다르면 포인터들이 지금과 다른 숫자를 가리킬때 까지 이동
                cnt_s = 0
                now_s = nums[s]
                while nums[s] == now_s:
                    cnt_s += 1
                    s += 1
            
                cnt_e = 0
                now_e = nums[e]
                while nums[e] == now_e:
                    cnt_e += 1
                    e -=1

                cnt += cnt_s * cnt_e # 같은 숫자들의 개수를 곱해서 개수 구함
                
        elif sum([nums[i], nums[s], nums[e]])<0: # 세개의 합이 음수이면 s를 오른쪽으로
            s += 1
        else: # 양수이면 e를 왼쪽으로
            e -= 1
print(cnt)
