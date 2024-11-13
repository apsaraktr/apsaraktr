
n=int(input('enter the limit:'))
s=0
for i in range (1,n):
    if (n%i==0):
        s=s+1
if(s==0):
   print('prime')
else:
   print('not prime')
