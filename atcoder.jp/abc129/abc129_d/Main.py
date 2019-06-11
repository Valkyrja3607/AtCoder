h,w=map(int,input().split())
s=[]
l=[[0 for i in range(w)]for j in range(h)]
 
for i in range(h):
    a=input()
    s.append(a)

yoko=[[0 for j in range(w)] for j in range(h)]
tate=[[0 for j in range(w)] for j in range(h)]

for i in range(h):
    p=0
    for j in range(w):
        if s[i][j]=="#" or j==w-1:
            if s[i][j]==".":
                for k in range(p):
                    yoko[i][j-k-1]+=p+1
                yoko[i][j]+=p+1
            else:
                for k in range(p):
                    yoko[i][j-k-1]+=p
            p=0
        elif s[i][j]==".":
            p+=1
for i in range(w):
    p=0
    for j in range(h):
        if s[j][i]=="#" or j==h-1:
            if s[j][i]==".":
                for k in range(p):
                    tate[j-k-1][i]+=p+1
                yoko[j][i]+=p+1
            else:
                for k in range(p):
                    tate[j-k-1][i]+=p
            p=0
        elif s[j][i]==".":
            p+=1
ans=0
for i in range(h):
    for j in range(w):
        ans=max(ans,yoko[i][j]+tate[i][j]-1)

print(ans)





