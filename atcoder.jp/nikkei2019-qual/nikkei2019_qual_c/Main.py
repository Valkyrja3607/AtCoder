n=int(input())
absa=[]


for i in range(n):
    c=[]
    c=[int(j) for j in input().split()]
    absa.append([c[0],c[1],c[1]+c[0]])


from operator import itemgetter
absa.sort(key=itemgetter(2))

t=0
k=0
for i in range(n):
    if i%2==0:
        t+=absa[-1][0]
        del absa[-1]
    else:
        k+=absa[-1][1]
        del absa[-1]
    
    

print(t-k)





