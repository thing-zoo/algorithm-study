budget = int(input())
stock = list(map(int, input().split()))
j_count, s_count = 0, 0
j_money, s_money = budget, budget
up_check, down_check = 0, 0

for i in range(len(stock)):
    if j_money >= stock[i]:
        j_count += j_money//stock[i]
        j_money %= stock[i]
    
    if i >= 3 and stock[i-3] < stock[i-2] < stock[i-1] < stock[i] and s_count > 0:
        s_money += stock[i]*s_count
        s_count = 0
    elif i >= 3 and stock[i-3] > stock[i-2] > stock[i-1] > stock[i] and s_money > stock[i]:
        s_count += s_money//stock[i]
        s_money %= stock[i]

j_total = j_money + stock[-1]*j_count
s_total = s_money + stock[-1]*s_count

if j_total > s_total:
    print("BNP")
elif j_total < s_total:
    print("TIMING")
else:
    print("SAMESAME")