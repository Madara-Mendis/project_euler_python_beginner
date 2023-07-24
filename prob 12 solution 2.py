#def TriNum(t):#calculating triangular numbers
#    if t==1:
#       return 1
#    else:
#        return(t+TriNum(t-1))
t=10000
while t>10:
    n=int((t*(t+1))/2)#calculating triangular numbers
    #n=TriNum(t)
    count=1
    if n%2==0:#counting even factors
        for even in range(2,n+2,2):
            if n%even==0:
                count+=1
    for odd in range(3,n,2):#counting odd factors
        if n%odd==0:
            count+=1
    print(count)
    if count>500:
               print(n)
               break
    else:
        t+=1
            
    
    
