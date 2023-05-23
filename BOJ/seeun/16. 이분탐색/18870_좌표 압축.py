n = int(input())
nums = list(map(int, input().split()))

# nums에 있는 숫자들을 중복 제거하고 오름차순 정렬
numset = set(nums)
numset = list(numset)
numset.sort()

# 작은 숫자부터 0~ 으로 좌표 압축
dic = {}
for i in range(len(numset)):
    dic[numset[i]] = i

# nums에 있는 숫자들을 압축된 좌표로 출력
for i in range(n):
    print(dic[nums[i]], end=" ")
