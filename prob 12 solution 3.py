n=1000
while n>0:
    t=int((n*(n+1))/2)
    count=0
    for i in range(2,t):
        if t%i==0:
            count+=1
            t//=i
    fac=2**count
    if fac>498:
        print((n*(n+1))/2)
        break
    else:
        n+=1
