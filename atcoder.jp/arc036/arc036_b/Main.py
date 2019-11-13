n=int(input())
h=[int(input()) for i in range(n)]
l=[]
p=-1
tmp=1
for i in range(n-1):
    if h[i]<h[i+1]:
        if p!=0:
            p=0
            l.append(tmp)
            tmp=1
        tmp+=1
    elif h[i]>h[i+1]:
        if p==0:
            p=1
        tmp+=1
    else:
        if p==1:
            l.append(tmp)
        p=-1
        tmp=1
l.append(tmp)

print(max(l))

