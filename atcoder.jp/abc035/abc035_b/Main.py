s=list(input())
t=int(input())
import collections
c=collections.Counter(s)
ans=abs(c["R"]-c["L"])+abs(c["U"]-c["D"])
if t==1:
    print(ans+c["?"])
else:
    if ans-c["?"]>=0:
        print(ans-c["?"])
    else:
        print((c["?"]-ans)%2)