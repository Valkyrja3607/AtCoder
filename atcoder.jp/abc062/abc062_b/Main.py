h,w=map(int,input().split())
a=[]
a.append("#"*(w+2))
for i in range(h):
    p="#"+input()+"#"
    a.append(p)
a.append("#"*(w+2))

for i in a:
    print(i)



