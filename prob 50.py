def Isprime(n):
    for i in range(3,n):
        if n%i==0:
            return 0
            break
    else:
        return 1
prime=[2]
tot=2
x=3
while x>0:
    if Isprime(x)==1:
        prime.append(x)
        tot+=x
        if tot>=1000000:
            tot-=x
            break
if Isprime(tot)==1:
    print(tot)
else:
    for y in prime:
        tot-=y
        if Isprime(tot)==1:
            print(tot)
            break
    x+=2
        
        
