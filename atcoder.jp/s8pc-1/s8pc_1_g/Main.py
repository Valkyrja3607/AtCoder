n,m=map(int,input().split());y=10**18;d,p,q=[[]for i in range(n)],[[[y,0]for j in range(n)]for i in range(1<<n)],[(0,0,0)];p[0][0]=[0,1]
for i in range(m):s,t,f,e=map(int,input().split());d[s-1].append((t-1,f,e));d[t-1].append((s-1,f,e));import heapq
while q:
  t,s,h=heapq.heappop(q)
  if t>p[h][s][0] or t>=p[-1][0][0]:continue
  for i,j,k in d[s]:
    m,r=h|(1<<i),p[h][s][1]
    if t+j<=k and h&(1<<i)==0:
      if p[m][i][0]>j+t:p[m][i]=[j+t,r];heapq.heappush(q,(j+t,i,m))
      elif p[m][i][0]==j+t:p[m][i][1]+=r
if p[-1][0][0]==y:print("IMPOSSIBLE")
else:print(*p[-1][0])