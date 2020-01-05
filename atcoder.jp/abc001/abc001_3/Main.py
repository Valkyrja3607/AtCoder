deg,dis = map(int,input().split())
 
dirs = ['N','NNE','NE','ENE','E','ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW']
n = deg*10 + 1125
n %= 36000
n //= 2250
D = dirs[n]
 
n = (3+dis) // 6
arr = [0,3,16,34,55,80,108,139,172,208,245,285,327]
W = 0
for x in arr[1:]:
    if x <= n:
        W += 1
 
if W == 0:
    D = 'C'
 
print(D,W)