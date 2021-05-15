h,w=map(int,input().split())
a=[input()for i in range(h)]
l=[[0]*w for i in range(h)]
for i in range(h)[::-1]:
    for j in range(w)[::-1]:
        if i==0 and j==0:
            if a[i][j]=="+":
                l[i][j]=1
            else:
                l[i][j]=-1
        if (i+j)%2==0:
            if a[i][j]=="+":
                l[i][j]-=1
            else:
                l[i][j]+=1
            if i==h-1 and j==w-1:
                continue
            elif i==h-1:
                l[i][j]+=l[i][j+1]
            elif j==w-1:
                l[i][j]+=l[i+1][j]
            else:
                l[i][j]+=max(l[i+1][j],l[i][j+1])
        else:
            if a[i][j]=="+":
                l[i][j]=1
            else:
                l[i][j]=-1
            if i==h-1 and j==w-1:
                continue
            elif i==h-1:
                l[i][j]+=l[i][j+1]
            elif j==w-1:
                l[i][j]+=l[i+1][j]
            else:
                l[i][j]+=min(l[i+1][j],l[i][j+1])
if l[0][0]==0:
    print("Draw")
elif l[0][0]>0:
    print("Takahashi")
else:
    print("Aoki")






