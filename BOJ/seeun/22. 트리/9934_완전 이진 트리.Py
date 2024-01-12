k = int(input())
nums = list(map(int, input().split()))
n = len(nums)

tree = [[] for _ in range(k)]
def find(arr, dep):
    if dep < k:
        loc = len(arr)//2 # 서브트리의 가운데 있는 숫자가 서브트리의 루트
        tree[dep].append(arr[loc]) # depth에 맞게 서브트리의 루트 담기
        find(arr[:loc], dep+1) # 왼쪽 트리 확인
        find(arr[loc:], dep+1) # 오른쪽 트리 확인

find(nums, 0)
for i in range(k):
    print(*tree[i])