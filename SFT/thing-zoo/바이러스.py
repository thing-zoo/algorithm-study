k, p, n = map(int, input().split())
print((k*pow(p, n, 1000000007))%1000000007) 
# int 오버플로우 날수있으므로, 나눠줘야함