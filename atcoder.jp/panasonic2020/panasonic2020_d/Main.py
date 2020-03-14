n=int(input())
ll=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

l=["a"]
for j in range(2,n+1):
    tmp=[]
    for s in l:
        m=len(set(list(s)))
        for i in ll[:m+1]:
            tmp.append(s+i)
    l=tmp

l.sort()
print('\n'.join(map(str,l)))



