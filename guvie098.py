i,j=map(int,input().split())
for k in range(i,j):
  tem=0
  x=k
while x>0:
  dig=(x%10)**3
  tem=tem+dig
  x=x//10
if (k==tem):
  print(k)
