
a=[21,34,11,65,78,222]
n=6
s=0
k=0
for i in range(n):

    if(a[i]%2==0):
      print("even",a[i])
      s=s+1
    else:
       print("odd",a[i])  
       k=k+1

print(s)
print(k)

output:

odd 21
even 34
odd 11
odd 65
even 78
even 222
3
3
