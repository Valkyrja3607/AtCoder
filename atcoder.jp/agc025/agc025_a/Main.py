n=int(input())

def f(n):
    n=str(n)
    r=0
    for i in range(len(n)):
        r+=int(n[i])
    return r

ans=100000000000
for i in range(1,n):
    ans=min(ans,f(i)+f(n-i))
print(ans)


