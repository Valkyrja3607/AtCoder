x=int(input())
import math
p=math.ceil(x**0.5)
ans=[1]
for i in range(2,p+1):
  j=2
  while True:
    if i**j<=x:
      ans.append(i**j)
    else:
      break
    j+=1
print(max(ans))
