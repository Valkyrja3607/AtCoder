n,q=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
ans={}
k_=[int(input())for i in range(q)]
k=sorted(k_)
i,j=0,0
cnt=0
while i<n and j<q:
    if k[j]+cnt<a[i]:
        ans[k[j]]=k[j]+cnt
        j+=1
    else:
        cnt+=1
        i+=1

for x in k[j:]:
    ans[x]=x+n

for i in k_:
    print(ans[i])