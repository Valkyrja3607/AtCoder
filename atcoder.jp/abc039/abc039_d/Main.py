h,w=map(int,input().split())
s=[]
s.append("#"*(w+2))
l=set()
for i in range(h):
    s.append("#"+input()+"#")
    for j in range(1,w+1):
        if s[-1][j]=="#":
            l.add((i,j-1))
s.append("#"*(w+2))
f=[]
for i in range(1,h+1):
    p=""
    for j in range(1,w+1):
        if s[i][j]=="#":
            c=0
            for x in range(i-1,i+2):
                for y in range(j-1,j+2):
                    if s[x][y]=="#":
                        c+=1
            if c==9:
                p+="#"
            else:
                p+="."
        else:
            p+="."
    f.append(p)
for i in range(h):
    for j in range(w):
        if f[i][j]=="#":
            c=0
            for x in range(i,i+3):
                for y in range(j,j+3):
                    if s[x][y]=="#":
                        if (x-1,y-1) in l:
                            l.remove((x-1,y-1))
                        c+=1
            if c==9:
                continue
            else:
                print("impossible")
                exit()

if l:
    print("impossible")
    exit()
print("possible")
for i in range(h):
    print(f[i])




