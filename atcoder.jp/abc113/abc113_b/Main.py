n=int(input())
t,a=map(int,input().split())
h=[int(i) for i in input().split()]

ans=100000000000000
p=0
for i in range(n):
    j=t-h[i]*0.006
    if ans>abs(j-a):
        ans=min(ans,abs(j-a))
        p=i+1

print(p)
    