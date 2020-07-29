a,b,c=list(map(int,input().split()))
if a==b==c:
  print(a)
elif a==b:
  print(c)
elif a==c:
  print(b)
else:
  print(a)
