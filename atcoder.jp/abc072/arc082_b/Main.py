n=int(input())
p=[int(i) for i in input().split()]

ans=0

if p[0]==1:
    ans+=1
    p[1]=1

for i in range(1,n):
    if p[i]==i+1:
        if p[i-1]==i:
            ans+=1
            p[i]=i
        else:
            if i+1!=n:
                if p[i+1]!=i+2:
                    ans+=1
                    p[i]=p[i-1]
            else:
                ans+=1

print(ans)