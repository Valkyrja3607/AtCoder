k=int(input())
if k<=500:
    n=k
    print(n)
    for i in range(n):
        print(*list(range(1,1+n)))
else:
    n=2*((k+3)//4)
    ans=[[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            ans[i][j]=(i+j)%n+1
            if i%2 and ans[i][j]+n<=k:
                ans[i][j]+=n
    print(n)
    for i in ans:
        print(*i)

