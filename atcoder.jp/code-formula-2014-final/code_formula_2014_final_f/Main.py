ans=[[]for i in range(100)]
for i in range(25):
    q,r=divmod(i,5)
    for a,(b,c) in zip([i,i+25,i+50,i+75],[[25,25],[250,250],[225,75],[100,200]]):
        ans[a]=[300*q+b,300*r+c]
for i,j in ans:print(i,j)