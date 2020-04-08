n=int(input());a=[int(input())for i in range(n)];d,b=[[0]*n for i in range(n)],0
for i in range(n):
  for l in range(n):
    r=(l+i)%n
    if(n-i)%2==1:t=max(d[(l+1)%n][r]+a[l],d[l][r-1]+a[r]);d[l][r]=t;b=max(b,t)
    else:
      if a[l]>a[r]:d[l][r]=d[(l+1)%n][r]
      else:d[l][r]=d[l][(r-1)%n]
print(b)