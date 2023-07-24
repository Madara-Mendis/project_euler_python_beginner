odd_mon=[4,6,9,11]
even_mon=[1,3,5,7,8,10,12]
week={'sun':0,'mon':1,'tue':2,'wed':3,'thu':4,'fri':5,'sat':6}
day=2
count=0
for year in range(1901,2001):
    #print(year)
    if year%100==0:
        if year%400==0:
            feb=29
        else:
            feb=28
    elif year%4==0:
        feb=29
    else:
        feb=28
    for num in range(1,13):
        print(day)
        if num in odd_mon:
            month=30
        elif num in even_mon:
            month=31
        else:
            month=feb
        remainder=month%7
        day+=(remainder)
        if day>=7:
            day-=7
        if day==0:
            count+=1
            #print('count',count)
        
print(count)
        
            
            
            
            
