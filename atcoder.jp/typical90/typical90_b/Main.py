n=int(input())
if n%2:
    print()
    exit()
ans=set()
import itertools
for l in itertools.combinations(range(n),n//2):
    l=set(l)
    tmp=0
    s=""
    for i in range(n):
        if i in l:
            s+="("
            tmp+=1
        else:
            s+=")"
            tmp-=1
        if tmp<0:
            break
    else:
        ans.add(s)
for i in sorted(list(ans)):
    print(i)