set_1=[]
myDic={}
lcm=1
for i in range(10,21):
    f=i
    factors=[]
    n=2
    while n<=i:
        if i%n==0:
            i/=n
            factors.append(n)
        else:
            n+=1
    print("fac(%d) ="%(f),factors)
    myDic[f]=factors
    set_1+=(factors)
set_fac=set(set_1)
print(set_fac)
print(myDic)
for items in set_fac:
    count=[]
    for val in myDic.values():
        count.append(val.count(items))
        max_count=max(count)
    lcm*=(items**max_count)
print(lcm)
