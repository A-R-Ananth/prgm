n=int(input())
s=list(map(int,str(n)))
t=list(map(lambda x:x**3,s))
if(sum(t)==n):
    print("yes ")
else:
    print("no ")
