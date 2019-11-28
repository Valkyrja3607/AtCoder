n=int(input())%30
m=(n//5)+1
s="123456"
ans=s[m:]+s[:m-1]
n%=5
ans=ans[:n]+str(m)+ans[n:]
print(ans)