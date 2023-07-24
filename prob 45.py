H=144
while H>0:
    p1=(1/6)+(((1/12)+(4*(H**2))-(2*H))**0.5)
    p2=(1/6)-(((1/12)+(4*(H**2))-(2*H))**0.5)
    print(p1,p2)
    if (isinstance(p1,int)==True) or (isinstance(p2,int)==True):
        value=H((2*H)-1)
        break
    H+=1
print(value)
