R,C=map(int,input().split())
sy,sx=map(int,input().split())
gy,gx=map(int,input().split())
sy-=1
sx-=1
gy-=1
gx-=1
c=[]
for i in range(R):
    c.append(input())

ans=[[10000 for i in range(C)] for j in range(R)]
ans[sy][sx]=0
q=[[sy,sx]]
p=0
w=0
while w==0:
    l=[[0,1],[0,-1],[1,0],[-1,0]]
    for i,j in l:
        if c[q[0][0]+i][q[0][1]+j]==".":
            if ans[q[0][0]+i][q[0][1]+j]>ans[q[0][0]][q[0][1]]+1:
                ans[q[0][0]+i][q[0][1]+j]=ans[q[0][0]][q[0][1]]+1
                q.append([q[0][0]+i,q[0][1]+j])
            
    q.remove(q[0])
    if q==[]:
        w+=1

print(ans[gy][gx])