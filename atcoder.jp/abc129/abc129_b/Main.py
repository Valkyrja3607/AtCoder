n=int(input())
w=[int(i) for i in input().split()]
sr=sum(w)
sl=0
ans=1000000000000000
for i in range(n-1):
    sr-=w[i]
    sl+=w[i]
    ans=min(ans,abs(sl-sr))

print(ans)