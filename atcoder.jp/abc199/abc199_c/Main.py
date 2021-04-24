n=int(input())
s=input()
q=int(input())
sl=list(s[:n])
sr=list(s[n:])
for i in range(q):
    t,a,b=map(int,input().split())
    if t==2:
        sl,sr=sr,sl
    else:
        if a<=n and b<=n:
            sl[a-1],sl[b-1]=sl[b-1],sl[a-1]
        elif a<=n:
            sl[a-1],sr[b-n-1]=sr[b-n-1],sl[a-1]
        elif a>n and b<=n:
            sl[b-1],sr[a-n-1]=sr[a-n-1],sl[b-1]
        else:
            sr[a-n-1],sr[b-n-1]=sr[b-n-1],sr[a-n-1]
ans="".join(sl)+"".join(sr)
print(ans)
