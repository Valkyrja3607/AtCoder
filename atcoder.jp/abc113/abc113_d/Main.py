h,w,k=map(int,input().split())

dp=[[0 for i in range(w+2)] for j in range(h+2)]

dp[0][1]=1

for i in range(h+1):
    for j in range(1,w+1):
        for l in range(2**(w-1)):
            p=bin(l)
            q=len(p)
            r=p.replace("11","")
            if q==len(r):
                r=p.replace("0b","")
                r="0"*(w-1-len(r))+r
                if j==1:
                    if r[0]=="0":
                        dp[i+1][j]+=dp[i][j]
                    else:
                        dp[i+1][j+1]+=dp[i][j]
                elif j==w:
                    if r[-1]=="0":
                        dp[i+1][j]+=dp[i][j]
                    else:
                        dp[i+1][j-1]+=dp[i][j]
                else:
                    if r[j-1]=="1":
                        dp[i+1][j+1]+=dp[i][j]
                    elif r[j-2]=="1":
                        dp[i+1][j-1]+=dp[i][j]
                    else:
                        dp[i+1][j]+=dp[i][j]
                   
print(dp[h][k]%1000000007)
        




