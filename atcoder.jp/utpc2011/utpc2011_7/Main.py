n,*l=map(int,open(0).read().split())
l.sort(reverse=True)
for i in range(n-5):
  if l[i]<l[i+1]+l[i+2]:
    a,b,c,d,e,f=l[i:i+6]
    if (a<b+c and d<e+f)or(a<b+d and c<e+f)or(a<b+e and c<d+f)or(a<b+f and c<d+e)or(a<c+d and b<e+f)or(a<c+e and b<d+f)or(a<c+f and b<d+e)or(a<d+e and b<c+f)or(a<d+f and b<c+e)or(a<e+f and b<c+d):
      print(a+b+c+d+e+f)
      exit()
    else:
      for j in range(i+3,n-2):
        x,y,z=l[j:j+3]
        if x<y+z:
          print(a+b+c+x+y+z)
          exit()
print(0)