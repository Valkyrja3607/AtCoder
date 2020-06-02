n,m,q=map(int,input().split())
abcd=[[int(j)for j in input().split()]for i in range(q)]
ans=0
import itertools
for l in itertools.combinations_with_replacement(range(1,m+1),n-1):
    tmp=0
    for a,b,c,d in abcd:
        p,q=0,0
        if a==1:
            p,q=l[b-2],1
        else:
            p,q=l[b-2],l[a-2]
        if p-q==c:
            tmp+=d
    ans=max(ans,tmp)
print(ans)