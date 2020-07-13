n=int(input())
S=input()
T=input()
for i in range(n):
    s,t=S[i],T[i]
    if s>t:t,s=s,t
    S=S.replace(t,s)
    T=T.replace(t,s)
x=len({s for s in S if s.isalpha()})-1
print(int((10-S[0].isalpha())*10**x))