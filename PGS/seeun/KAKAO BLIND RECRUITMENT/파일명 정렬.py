# 내가 짠 코드
def solution(files):
    n = len(files)
    answer = []
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    change = [[] for _ in range(len(files))]
    for k in range(len(files)):
        f = list(files[k])
        numstart, numend = 101, 0
        for i in range(10):
            if nums[i] in f:
                numstart = min(numstart,f.index(nums[i]))
                numend = numstart
                for j in range(numstart, min(numstart+5, len(f))):
                    if f[j] in nums:
                        numend = j
                    else:
                        break
                
        numend += 1

        change[k] = ["".join(f[:numstart]), "".join(f[numstart:numend]), "".join(f[numend:])]

    change.sort(key = lambda x:(x[0].lower(), int(x[1])))
    for i in range(n):
        answer.append("".join(change[i]))
    return answer

# --------- # ---------# ---------# ---------# ---------# ---------# ---------# ---------

# 검색해서 따라한 코드
def solution(files):
    n = len(files)
    answer = []
    change = []
    for f in files:
        for i in range(len(f)):
            if f[i].isdecimal():
                numstart, numend = i, 0
                for j in range(numstart, min(numstart+5, len(f))):
                    if f[j].isdecimal():
                        numend = j
                    else:
                        break

                numend += 1
                break

        change.append(["".join(f[:numstart]), "".join(f[numstart:numend]), "".join(f[numend:])])

    change.sort(key = lambda x:(x[0].lower(), int(x[1])))
    for i in range(n):
        answer.append("".join(change[i]))
    return answer