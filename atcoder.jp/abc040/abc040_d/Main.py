n,m=[int(j) for j in input().split()]
aby=[[int(j) for j in input().split()]for i in range(m)]
q=int(input())
vw=[[int(j) for j in input().split()]+[i] for i in range(q)]

par=[-1 for i in range(n+1)]    #par<0なら自身が親で要素の個数、>0なら子で親の位置示す

def root(a):
    if par[a]<0:
        return a
    else:
        return root(par[a])

def size(a):
    return -par[root(a)]

def connect(a,b):
    a=root(a)
    b=root(b)
    if a==b:
        return False
    if size(a)<size(b):
        a,b=b,a
    par[a]+=par[b]
    par[b]=a
    return True


from operator import itemgetter
aby.sort(key=itemgetter(2),reverse=True)
vw.sort(key=itemgetter(1),reverse=True)
ans=[0]*q
i=0
for v,w,idx in vw:
    if i<m:
        while aby[i][2]>w:
            a,b,y=aby[i]
            connect(a,b)
            i+=1
            if i==m:
                break
    ans[idx]=-par[root(v)]

print('\n'.join(map(str,ans)))