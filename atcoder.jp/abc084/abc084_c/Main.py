n=int(input())

c=[]
s=[]
f=[]

for i in range(n-1):
    x,y,z=map(int,input().split())
    c.append(x)
    s.append(y)
    f.append(z)
    
for i in range(n):
    ans=0
    if i<n-2:
        j=i
        ans=c[j]+s[j]
        while j<n-2:
            if ans>=s[j+1]:
                if ans%f[j+1]==0:
                    ans+=c[j+1]
                else:
                    ans+=c[j+1]+f[j+1]-ans%f[j+1]
            else:
                ans=c[j+1]+s[j+1]                
            j+=1
        print(ans)
    elif i==n-2:
        print(c[n-2]+s[n-2])
    elif i==n-1:
        print(0)