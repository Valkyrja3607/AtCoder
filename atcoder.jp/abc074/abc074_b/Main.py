n=int(input())
k=int(input())
x=[min(int(j),k-int(j)) for j in input().split()]
print(2*sum(x))