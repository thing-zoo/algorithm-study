import sys
input = sys.stdin.readline
def find_gcd(a, b):
    if a == 0: return b
    return find_gcd(b%a, a)
n = int(input())
data = list(map(int, input().rstrip().split()))
if n == 2:
    gcd = find_gcd(data[0], data[1])
else:
    gcd = find_gcd(find_gcd(data[0], data[1]), data[2])
for i in range(1, gcd+1):
    if gcd%i==0:
        sys.stdout.write(str(i)+'\n')