def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(10):
        s = s.replace(words[i], str(i)) # 문자열 자체가 변환되진 않고 반환함
    return int(s)