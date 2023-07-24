count=1
n=3
while n>2:
    for i in range(2,n):
        if n%i==0:
            break
    else:
        count+=1
        if count==10001:
            print("%d th prime number is %d"%(count,n))
            break
    n+=1
    
