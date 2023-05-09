x = int(input())
## 내 코드
# if x == 1:
#     print("1/1")
# else:
#     i = 0
#     while i*(i+1)//2 < x:
#         i += 1
#     i -= 1
#     if i%2 != 0:
#         print("%d/%d" %(x-(i*(i+1)//2), (i+1)-(x-(i*(i+1)//2))+1))
#     else:
#         print("%d/%d" %((i+1)-(x-(i*(i+1)//2))+1, x-(i*(i+1)//2)))

## 정답코드
line = 1 # 대각선 번호
while x > line:
    x -= line
    line += 1
    
if line%2 == 0:
    a = x
    b = line-x+1
else:
    a = line-x+1
    b = x
    
print(a, '/', b, sep='')