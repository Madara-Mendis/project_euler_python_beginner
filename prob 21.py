def amicable(n):
    tot=1
    if n%2==0:
        for i in range(2,n):
            if n%i==0:
                tot+=i
    else:
        for i in range(3,n,2):
            if n%i==0:
                tot+=i
    return tot
amic=[]
num=3
for num in range(3,10000):
    if not num in amic:
        print('num',num)
        tot1=amicable(num)
        print('tot1',tot1)
        tot2=amicable(tot1)
        print('tot2',tot2)
        if num==tot2:
            if tot1!=tot2:
                amic.append(num)
                amic.append(tot1)
                print(amic)
print('sum of amic num =',sum(amic))
