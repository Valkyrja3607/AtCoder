a=input()
b=input()
n=len(a)
import collections
l1=collections.Counter(list(a))
l2=collections.Counter(list(b))

if l1!=l2:
    print("NO")
    exit()

cn=0
s1=[]
s2=[]
l=[]
for i,j in zip(a,b):
    if i!=j:
        s1.append(i)
        s2.append(j)
        cn+=1
    else:
        l.append(i)
c=collections.Counter(l)
ll=c.most_common()
stock=[list(tup) for tup in ll]

if cn>6:
    print("NO")

else:
    while len(s1)<6:
        if len(s1)==n:
            break
        stock[0][1]-=1
        s1.append(stock[0][0])
        s2.append(stock[0][0])
        if stock[0][1]==0:
            del stock[0]
    import itertools
    cn=len(s1)
    swaps=list(itertools.combinations(list(range(cn)),2))
    for p in itertools.product(swaps,repeat=3):
        s=s1.copy()
        for i,j in p:
            s[i],s[j]=s[j],s[i]
        if s==s2:
            print("YES")
            exit()
    print("NO")






