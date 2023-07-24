n=1000000
while n>10000:
    T=int((n*(n+1))/2)
    fac_T=[]
    for i in range(2,T):
        if T%i==0:
            fac_T.append(i)
    print(len(fac_T))
    if len(fac_T)>=498:
        print('your triangle number:',T)
        break
    else:
        n+=1
    
