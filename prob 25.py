a=89
b=144
count=12
while b>0:
    if len(str(b))==1000:
        print(count)
        break
    a,b=b,a+b
    count+=1
