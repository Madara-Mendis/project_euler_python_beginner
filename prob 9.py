def pyTriplet():
    for a in range(1000,0,-1):
        for b in range(a-1,0,-1):
            x=a*a+b*b
            c=x**(0.5)
            if c==round(c):
                if a+b+c==1000:
                    product=(a*b*c)
                    return product

print('product:',pyTriplet())
    
