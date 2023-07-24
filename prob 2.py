a=1
b=2
tot=0
while a<=4000000:
    if a%2==0:
        tot+=a
    a,b=b,a+b
print(tot)
        
