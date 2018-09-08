n=int(input())

w=[]
ans=0

for i in range(n):
    a=input()
    w.append(a)
    if i>0:
        if w[i][0]==w[i-1][-1]:
            ans+=1

li=list(set(w))
l=len(li)

if l==n and ans==n-1:
    print("Yes")
else:
    print("No")
    
