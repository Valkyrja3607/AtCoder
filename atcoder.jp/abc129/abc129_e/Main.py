l=input()
mod=10**9+7
n,m=1,0
for i in l:
    if i=="1":
        m=(m*3+n)%mod
        n=n*2%mod
    else:
        m=m*3%mod
print((n+m)%mod)
