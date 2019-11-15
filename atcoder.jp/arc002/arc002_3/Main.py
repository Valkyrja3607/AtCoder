n=int(input())
c=input()
ans=10**18
for i in "ABXY":
    for j in "ABXY":
        for k in "ABXY":
            for l in "ABXY":
                s=c
                L=i+j
                R=k+l
                s=s.replace(L,"L").replace(R,"R")
                ans=min(ans,len(s))
print(ans)