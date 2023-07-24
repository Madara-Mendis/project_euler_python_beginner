square=[1,4,9,16,25,36,49,64,81,100]
prime=[2]
n=3
while n>0:
    for i in range(3,n):
        if n%i==0:
            x=n
            for a in prime:
                B=(x-a)/2
                if B in square:
                    break
            else:
                print x
                break
            break
    else:
        prime.append.n
    n+=2
                
