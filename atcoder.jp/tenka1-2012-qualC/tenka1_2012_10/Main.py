s=input().replace("10","T")
from collections import Counter
l=Counter()
n=len(s)
ans=""
for i in range(0,n,2):
    if s[i+1] in "TJQKA":
        l[s[i]]+=1
        if l[s[i]]==5:
            for j in range(0,n,2):
                if s[j]!=s[i] or s[j+1] not in "TJQKA":
                    ans+=s[j:j+2]
                elif s[j+1]==s[i+1]:
                    if ans!="":
                        print(ans.replace("T","10"))
                    else:
                        print(0)
                    exit()