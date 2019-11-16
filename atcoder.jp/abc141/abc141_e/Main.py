n=int(input())
s=input()
ans=0
def z_algo(S):
    N=len(S)
    A=[0]*N
    i=1;j=0
    A[0]=l=len(S)
    while i<l:
        while i+j<l and S[j]==S[i+j]:
            j+=1
        if not j:
            i+=1
            continue
        A[i]=j
        k=1
        while l-i>k<j-A[k]:
            A[i+k]=A[k]
            k+=1
        i+=k;j-=k
    return A

for i in range(n):
    l=z_algo(s[i:])
    m=len(l)
    for j in range(m):
        ans=max(ans,min(j,l[j]))
print(ans)





