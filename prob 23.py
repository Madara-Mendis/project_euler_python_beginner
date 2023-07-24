#finding abundant integers
abundant=[]
for num in range(2,28123):
    tot=1
    if num%2==0:
        for i in range(2,num):
            if num%i==0:
                 tot+=i
    else:
        for i in range(3,num,2):
            if num%i==0:
                 tot+=i
    if tot>num:
        abundant.append(num)
        print(abundant)
#finding the numbers which is created by adding 2 abundant integers
integer=[]
l=len(abundant)
for a in range(0,l):
    for b in range(0,l):
        c=a+b
        if c<=28123:
            integer.append(c)
print(integer)
#finding sum of non-abundant numbers below 28123
for x in range(1,28124):
    if not y in integer:
        sum_abundant+=y
print('total',sum_abundant)
    
    
        
