n=int(input())
ls=[]
lt=[]
for i in range(n):
    s,t=input().split()
    ls.append(s)
    lt.append(int(t))
x=input()
ans=sum(lt)
tmp=0
for i in range(n):
    tmp+=lt[i]
    if ls[i]==x:
        ans-=tmp
        print(ans)
        exit()




