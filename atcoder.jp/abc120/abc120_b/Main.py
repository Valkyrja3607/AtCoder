a,b,k=map(int,input().split())
ans=[]
c=0
for i in range(1,101):
    if a%i==0 and b%i==0:
        ans.append(i)
print(ans[-1*k])