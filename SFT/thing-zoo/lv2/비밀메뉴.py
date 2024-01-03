m,n,k = map(int, input().split())
secret = input()
user = input()
if secret in user:
    print("secret")
else:
    print("normal")