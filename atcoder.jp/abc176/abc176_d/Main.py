from collections import defaultdict, deque

def solve():
    h,w=map(int,input().split())
    ch,cw=[int(j)-1 for j in input().split()]
    dh,dw=[int(j)-1 for j in input().split()]
    s=[input() for i in range(h)]
    q=deque([(ch,cw)])
    d=[(1,0),(-1,0),(0,1),(0,-1)]
    inf=10**7
    dp=[[inf]*w for i in range(h)]
    dp[ch][cw]=0
    while q:
        i,j=q.popleft()
        if (i,j)==(dh,dw):
            print(dp[i][j])
            exit()
        for x,y in d:
            if 0<=i+x<h and 0<=j+y<w and s[i+x][j+y]=="." and dp[i+x][j+y]>dp[i][j]:
                dp[i+x][j+y]=dp[i][j]
                q.appendleft((i+x,j+y))
        for x in range(-2,3):
            for y in range(-2,3):
                if 0<=i+x<h and 0<=j+y<w and s[i+x][j+y]=="." and  dp[i+x][j+y]>dp[i][j]+1:
                    dp[i+x][j+y]=dp[i][j]+1
                    q.append((i+x,j+y))
    print(-1)


if __name__ == '__main__':
    solve()