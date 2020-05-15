s,t=input().split()
s=int(s.replace("B","-").replace("F",""))
t=int(t.replace("B","-").replace("F",""))
print(abs(s-t)-int(s*t<0))