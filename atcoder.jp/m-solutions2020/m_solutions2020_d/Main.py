n=int(input())
a=[int(j) for j in input().split()]
l=a[:2]
if a[0]<=a[1]:b=True
else:b=False
for i,j in zip(a,a[1:]):
    if i<j:
        if b:
            l[-1]=j
        else:
            l.append(j)
            b=True
    elif i>j:
        if b:
            l.append(j)
            b=False
        else:
            l[-1]=j
ans=1000
for i,j in zip(l,l[1:]):
    if i<j:
        ans=(ans//i)*j+ans%i
print(ans)