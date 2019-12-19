def f():
    import sys
    import numpy as np
    input=sys.stdin.readline
    n=int(input())
    a=np.array([0]+[int(j) for j in input().split()])
    np.cumsum(a,out=a)
    dp=np.zeros((n,n+1),np.int64)

    for i in range(1,n):
        l=np.arange(n-i)
        r=np.arange(i+1,n+1)
        m=(np.arange(1,i+1)+l[:,np.newaxis]).T
        dp[l,r]=np.amin(dp[l,m]+dp[m,r],0)+a[r]-a[l]
    print(dp[0][n])
f()