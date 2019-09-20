h,w=map(int,input().split())
l=[]
ll=[[1,0],[-1,0],[0,-1],[0,1],[1,1],[-1,1],[1,-1],[-1,-1]]
ans=[[0]*w for i in range(h)]
s=set()
for i in range(h):
    tmp=input()
    l.append(tmp)
    for j in range(w):
        if tmp[j]=="#":
            ans[i][j]="#"
            for x,y in ll:
                if 0<=i+x<h and 0<=j+y<w:
                    if ans[i+x][j+y]!="#":
                         ans[i+x][j+y]+=1
for i in range(h):
    tmp=""
    for j in range(w):
        tmp+=str(ans[i][j])
    print(tmp)
