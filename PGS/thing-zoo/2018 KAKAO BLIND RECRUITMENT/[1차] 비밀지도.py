def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        temp = str(bin(arr1[i] | arr2[i]))[2:]
        temp = (n-len(temp))*'0' + temp
        temp = temp.replace('1', '#')
        temp = temp.replace('0', ' ')
        answer.append(temp)
    return answer