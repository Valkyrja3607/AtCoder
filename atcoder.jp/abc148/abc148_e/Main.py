n=int(input())
if n%2==1 or n<=9:
    print(0)
    exit()
ans=n//10
i=5
while True:
    ans+=n//(10*i)
    i*=5
    if n<(10*i):
        break
print(ans)