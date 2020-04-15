x,y,a,b,c=[int(j) for j in input().split()]
p=[int(j) for j in input().split()]
q=[int(j) for j in input().split()]
r=[int(j) for j in input().split()]

p.sort(reverse=True)
q.sort(reverse=True)
r.sort(reverse=True)
l=p[:x]+q[:y]
l.sort()
ans=sum(l)
for i in l:
    if r!=[]:
        if i<r[0]:
            ans+=r[0]-i
            del r[0]
        else:
            break
    else:
        break
print(ans)