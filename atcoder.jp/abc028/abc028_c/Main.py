a=[int(i) for i in input().split()]
ans=[]

s=sum(a)

ans.append(s-a[0]-a[1])
ans.append(s-a[0]-a[2])
ans.append(s-a[0]-a[3])
ans.append(s-a[0]-a[4])
ans.append(s-a[1]-a[2])
ans.append(s-a[1]-a[3])
ans.append(s-a[1]-a[4])
ans.append(s-a[2]-a[3])
ans.append(s-a[2]-a[4])
ans.append(s-a[3]-a[4])

an=list(set(ans))
an.sort()

print(an[-3])
