s=int(input())
if s==10**18:
    print(0,0,10**9,0,0,10**9)
    exit()
print(0,0,10**9,1,10**9-s%(10**9),s//(10**9)+1)