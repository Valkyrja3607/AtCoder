x=[]
y=[]
z=[]

for i in range(3):
    a,b,c=map(int,input().split())
    x.append(a-b)
    y.append(a-c)
    z.append(b-c)

if x[0]==x[1] and x[1]==x[2] and y[0]==y[1] and y[1]==y[2] and z[0]==z[1] and z[1]==z[2]:
    print("Yes")
else:
    print("No")