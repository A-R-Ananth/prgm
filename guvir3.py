from itertools import combinations
strin,num=map(int,input().split())
i=len(str(strin))
k=list(combinations(str(strin),i-num))
k=(sorted(k))
t="".join(k[0])
print(t)
