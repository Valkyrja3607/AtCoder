n=int(input())
s=input()
dp={i:[0]*n for i in "atcoder"}
mod=10**9+7
for idx,j in enumerate(s):
    for i in "atcoder":
        dp[i][idx]=dp[i][idx-1]
    if j=="a":
        dp[j][idx]+=1
    elif j=="t":
        dp[j][idx]=(dp["a"][idx]+dp[j][idx])%mod
    elif j=="c":
        dp[j][idx]=(dp["t"][idx]+dp[j][idx])%mod
    elif j=="o":
        dp[j][idx]=(dp["c"][idx]+dp[j][idx])%mod
    elif j=="d":
        dp[j][idx]=(dp["o"][idx]+dp[j][idx])%mod
    elif j=="e":
        dp[j][idx]=(dp["d"][idx]+dp[j][idx])%mod
    elif j=="r":
        dp[j][idx]=(dp["e"][idx]+dp[j][idx])%mod
print(dp["r"][-1]%mod)