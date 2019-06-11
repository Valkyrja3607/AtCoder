n=int(input())
mod=10**9+7

def d(s):
    if "AGC" in s:
        return False
    for i in range(3):
        l=list(s)
        l[i],l[i+1]=l[i+1],l[i]
        if "AGC" in "".join(l):
            return False
    return True

m=[{} for i in range(n+1)]
def f(num,s):
    if s in m[num]:
        return m[num][s]
    if num==n:
        return 1
    ans=0
    for c in "ACGT":
        if d(s+c):
            ans=(ans+f(num+1,s[1:3]+c))%mod
    m[num][s]=ans
    return ans

print(f(0,"PPP"))
        
        



