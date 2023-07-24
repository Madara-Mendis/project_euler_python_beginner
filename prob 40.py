tot=1
num='1'
x=2
while x>0:
    num+=str(x)
    print(num)
    if len(str(num))==1000000:
        print(num)
        y=1
        while y<=1000000:
            tot*=int((str(num))[y-1])
            y*=10
        print(tot)
        break
    x+=1
