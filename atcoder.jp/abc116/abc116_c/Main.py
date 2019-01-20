n=int(input())
h=[int(i) for i in input().split()]

ans=0

while sum(h)!=0:
    k=ans
    for i in range(n):
        if i==0 and h[i]!=0:
            ans+=1
        elif h[i]!=0 and h[i-1]==0:
            ans+=1
    if k==ans:
        ans+=1
        
    for i in range(n):
        if h[i]!=0:
            h[i]-=1


        
print(ans)
            
            
        




