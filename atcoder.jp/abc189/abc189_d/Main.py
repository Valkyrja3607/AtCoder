n=int(input())
s=[input() for i in range(n)]
l=[]
for i in range(n):
    if s[i]=="OR":
        l.append(i)
if len(l)==0:
    print(1)
else:
    ans=0
    for i in l:
        ans+=pow(2,i+1)
    print(ans+1)