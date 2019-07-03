d=input()
c=c.lower()
if d in ['a','e','i','o','u']:
  print('vovel')
elif ord(d) in range(97,123):
  print('Consonant')
else:
  print('invalid')  
