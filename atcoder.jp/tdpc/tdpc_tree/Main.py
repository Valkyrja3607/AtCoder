import math as m;N=int(input());E=[[]for _ in range(N+1)]
for _ in range(N-1):a,b=map(int,input().split());E[a].append(b);E[b].append(a)
D=[[-1]*(N+1)for _ in range(N+1)];S=[[0]*(N+1)for _ in range(N+1)];a=0
def f(i,j):
 if D[i][j]==-1:
  D[i][j]=0
  for k in E[j]:
   if k!=i:f(j,k);S[i][j]+=S[j][k]
  S[i][j]+=1
  R=m.factorial(S[i][j]-1)
  for k in E[j]:
   if k!=i:R=R*D[j][k]//m.factorial(S[j][k])
  D[i][j]=R;return D[i][j]
for i in range(1,N+1):a+=f(0,i)
print((a//2)%(10**9+7))