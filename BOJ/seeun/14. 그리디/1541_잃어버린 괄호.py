string = input()
# 첫번째 글자가 -인 경우
minus = False
if string[0] == '-':
    minus = True
nums = string.split("-")

res = 0
if not minus: #첫글자가 마이너스면 첫번째에 빈 문자열이 들어가있음 -> 마이너스가 아니면 첫번째도 더해줌
    tmp = list(map(int, nums[0].split("+")))
    res += sum(tmp)
for i in range(1, len(nums)):
    tmp = list(map(int, nums[i].split("+")))
    res -= sum(tmp)
print(res)
