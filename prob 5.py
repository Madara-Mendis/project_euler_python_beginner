x=140000
while x>0:
    i=20
    while i>10:
        if x%i==0:
            i-=1
        else:
            x+=1
            i=20
            print(x)
    break
print("your output is:",x)
