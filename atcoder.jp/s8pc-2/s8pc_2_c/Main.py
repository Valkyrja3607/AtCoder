from subprocess import*
call(('pypy3','-c',"""
n="0"+input()
d=int(input())
D=[[0]*(d+1)for i in range(len(n))]
D[0][0]=1
for i in range(2,len(n)+1):
  for j in range(1,10):
    if i-j<1:break
    x=int(n[i-j:i])
    if x>d:break
    for k in range(d+1):
      if D[i-j-1][k]>0 and k+x<=d:
        D[i-1][k+x]+=D[i-j-1][k]
print(sum(D[-1])%(10**9+7))
"""))
