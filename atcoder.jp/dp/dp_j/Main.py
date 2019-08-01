n=int(input())
dp=[[[0.0]*(n+1) for i in range(n+1)] for j in range(n+1)]
dp[0][0][0]=0
a=[float(i) for i in input().split()]

p=a.count(1)
q=a.count(2)
r=a.count(3)

l=[1]
for i in range(1,1000):
    l.append(1.0/i)

for k in range(r+1):
    for j in range(q+r-k+1):
        for i in range(n-k-j+1):
            if i==j==k==0:
                continue
            res=n
            if i>0:
                res+=i*dp[i-1][j][k]
            if j>0:
                res+=j*dp[i+1][j-1][k]
            if k>0:
                res+=k*dp[i][j+1][k-1]
            res*=1/(i+j+k)
            dp[i][j][k]=res

print(dp[p][q][r])
