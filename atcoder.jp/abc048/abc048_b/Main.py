a,b,x=map(int,input().split())

if a%x==0:
    nl=a
else:
    nl=a-a%x+x
if b%x==0:
    nr=b
else:
    nr=b-b%x

print((nr-nl)//x+1)