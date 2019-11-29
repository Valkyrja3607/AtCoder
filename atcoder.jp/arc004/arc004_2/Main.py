n=int(input())
d=[int(input()) for i in range(n)]
s=sum(d)
print(s)
if n==1:
    print(d[0])
    exit()
elif n==2:
    print(abs(d[0]-d[1]))
    exit()
else:
    from itertools import accumulate
    l=list(accumulate(d))
    import itertools
    ans=s
    t=0
    for i,j in itertools.combinations(list(range(n)),2):
        if i>j:
            i,j=j,i
        a,b,c=l[i],l[j]-l[i],s-l[j]
        ans=min(ans,abs(a+b-c),abs(a-b-c),abs(a-b+c))
        if a+b>=c and a+c>=b and b+c>=a:
            print(0)
            exit() 

print(ans)