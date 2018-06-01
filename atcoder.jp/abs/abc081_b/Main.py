n=int(input())

a = [int(n) for n in input().split()]

i=0
while all(j%2==0 for j in a):
    a=[j/2 for j in a]
    i+=1
    continue
print(i)