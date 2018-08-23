n=int(input())
s=input()

a=0
b=0
e=[]
w=[0]
ans=[]

for i in s:
    if i==("E"):
        a+=1
    else:
        b+=1
    e.append(a)
    w.append(b)
        
for i in range(n):
    ans.append(e[n-1]-e[i]+w[i])

print(min(ans))