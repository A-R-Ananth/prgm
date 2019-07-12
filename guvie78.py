n=int(input("Enter the no: "))
t=list(map(int,str(n)))
s=list(map(lambda x:x**3,t))
if(sum(s)==n):
    print("yes ")
else:
    print("no ")
