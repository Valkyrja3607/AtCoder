d,n=map(int,input().split())
t=[int(input()) for i in range(d)]
from numpy import *
dp=array([[-1]*n for i in range(d)])
l=array([[int(j) for j in input().split()] for i in range(n)])

for i in range(d):
    tmp=t[i]
    if i==0:
        for j in range(n):
            a,b,c=l[j]
            if a<=tmp<=b:
                dp[0][j]=c
    elif i==1:
        for j in range(n):
            a,b,c=l[j]
            if a<=tmp<=b:
                dp[i][j]=max(dp[i][j],(abs(l[dp[i-1]>=0][:,2]-c)).max())
    else:
        for j in range(n):
            a,b,c=l[j]
            if a<=tmp<=b:
                dp[i][j]=max(dp[i][j],(abs(l[dp[i-1]>=0][:,2]-c)+dp[i-1][dp[i-1]>=0]).max())

print(dp[-1].max())
