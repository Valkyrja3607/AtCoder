n=int(input())
ans=0
import itertools
for i in range(1,n+1):
    p,q=str(i)[0],str(i)[-1]
    if int(p)*int(q)==0:
        continue
    if len(str(i))>=3:
        if p<q:
            ans+=int("1"*(len(str(i))-2))*2
        elif p>q:
            ans+=int("1"*(len(str(i))-1))*2
        else:
            ans+=int("1"*(len(str(i))-2))*2
            ans+=(int(str(i)[1:-1])+1)*2
            ans+=1
    elif len(str(i))==1:
        ans+=1
    else:
        if p>q:
            ans+=2
        elif p==q:
            ans+=3
print(ans)
