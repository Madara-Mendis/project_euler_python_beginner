x=987654321
while x>9000:
    n=len(str(x))
    for num in range(1,n+1):
        if not str(num) in str(x):
            break
    else:
        print(x)
        for i in range(3,int(x/2)):
            if x%i==0:
                break
        else:
            print('largest',x)
            break
    x-=2
        
            
    
