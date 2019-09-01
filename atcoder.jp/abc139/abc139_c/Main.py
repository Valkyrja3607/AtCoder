n=int(input())
h=[int(i) for i in input().split()]
h.append(10**18)
ans=0
tmp=0
for i in range(n):
    if h[i]>=h[i+1]:
        tmp+=1
    else:
        tmp=0
    ans=max(ans,tmp)
ans=max(ans,tmp)
print(ans)