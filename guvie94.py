n=int(input())
p=list(map(int,str(n)))
q=list(map(lambda x:x**3,p))
if(sum(q)==n):
    print("yes ")
else:
    print("no ")
