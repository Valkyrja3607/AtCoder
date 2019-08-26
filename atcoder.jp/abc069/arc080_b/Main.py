h,w=map(int,input().split())
n=int(input())
a=[int(j) for j in input().split()]
ans=[[0 for i in range(w)] for j in range(h)]
i,j=0,0
for p in range(n):
    for q in range(a[p]):
        ans[i][j]=p+1
        if j==w-1 and i%2==0:
            i+=1
        elif j==0 and i%2==1:
            i+=1
        elif i%2==0:
            j+=1
        elif i%2==1:
            j-=1

for i in ans:
    print(*i)