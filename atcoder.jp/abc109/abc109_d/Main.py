h,w=map(int,input().split())
a=[]
s=0
for i in range(h):
    p=[int(j) for j in input().split()]
    a.append(p)
    s+=sum(p)
ans=[]
if s%2==0:
    if a[0][0]%2==1:
        if w!=1:
            ans.append([1,1,1,2])
            a[0][1]+=1
        elif h!=1:
            ans.append([1,1,2,1])
            a[1][0]+=1
else:
    if a[0][0]%2==0:
        if w!=1:
            ans.append([1,1,1,2])
            a[0][1]+=1
        elif h!=1:
            ans.append([1,1,2,1])
            a[1][0]+=1

for i in range(h):
    for j in range(w):
        if i==0 and j==0:
            continue
        if j==w-1:
            if i!=h-1:
                if a[i][j]%2==1:
                    ans.append([i+1,j+1,i+2,j+1])
                    a[i+1][j]+=1
        else:
            if a[i][j]%2==1:
                ans.append([i+1,j+1,i+1,j+2])
                a[i][j+1]+=1

print(len(ans))
for a,b,c,d in ans:
    print(a,b,c,d)




