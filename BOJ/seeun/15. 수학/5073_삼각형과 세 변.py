a, b, c = map(int, input().split())
while a!=0 or b!=0 or c!=0:
    if max([a, b, c]) >= (a+b+c)-max([a, b, c]): # 삼각형의 조건
        print('Invalid')
    elif a!=b and b!= c and a!= c: # 모두 다름
        print('Scalene')
    elif a==b and b==c: # 모두 같음
        print("Equilateral")
    elif a==b or b== c or a==c: # 두 변만 같음
        print('Isosceles')
    
    a, b, c = map(int, input().split())

    