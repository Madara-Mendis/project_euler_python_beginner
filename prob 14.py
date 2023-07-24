def collatz(n):
     global c
     if n==1:
        return c
     elif n%2==0:
        c+=1 
        return(collatz(n/2))
     else:
        c+=1
        return(collatz((3*n)+1))
     

maxi=1
output=1
for num in range(999999,9000,-1):
    c=1
    count=(collatz(num))
    print(count)
    if count>maxi:
        maxi=count
        output=num
print(output,maxi)
    
