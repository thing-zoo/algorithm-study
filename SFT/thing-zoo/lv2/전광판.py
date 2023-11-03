bulbs = {
    '0':'1111011', 
    '1':'0001010', 
    '2':'0110111', 
    '3':'0011111',
    '4':'1001110',
    '5':'1011101', 
    '6':'1111101',
    '7':'1001011',
    '8':'1111111',
    '9':'1011111',
    ' ':'0000000'
}
for _ in range(int(input())):
    a, b = input().split()
    a = (5-len(a))*' ' + a 
    b = (5-len(b))*' ' + b
    
    answer = 0
    for i in range(5):
        for j in range(7):
            if bulbs[a[i]][j] != bulbs[b[i]][j]: 
                answer += 1
    print(answer)
