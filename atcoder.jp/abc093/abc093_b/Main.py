a,b,k=map(int,input().split())
print(*sorted(list(set(list(range(a,min(a+k,b+1)))+list(range(max(b+1-k,a),b+1))))),sep="\n")