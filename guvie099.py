i,j=map(int,input().split())
for k in range(i,j):
  tem=0
  y=k
while y>0:
  dig=(y%10)**3
  tem=tem+dig
  x=y//10
if (k==tem):
  print(k)
