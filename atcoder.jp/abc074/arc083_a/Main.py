a,b,c,d,e,f=map(int, input().split())
 
W=[100*a*x + 100*b*y for x in range(0,31) for y in range(0,31) if 0<(100*a*x+100*b*y)<=f]
S=[c*x+d*y for x in range(0,3001) for y in range(0,3001) if 0<(c*x+d*y)<=f]
 
dense = 0
sugar = 0
mass = 100*a
for w in W:
    for s in S:
        if (w+s<=f and s<=(w*e/100) and dense*(s+w)<s):
            dense=s/(s+w)
            sugar=s
            mass=s+w
print(mass,sugar)