participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

def solution(participant, completion):
    answer = ''
    finish = {}
    for p in participant:
        if p not in finish:
            finish[p] = 1
        else:
            finish[p] += 1
    for c in completion:
        if c in finish:
            finish[c] -= 1
  
    for c in finish:
        if finish[c] == 1:
            answer = c
            break
   
    return answer

solution(participant, completion)