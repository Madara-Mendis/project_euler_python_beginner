num=[]
for a in range(2,101):
    for b in range(2,101):
        print(a,b)
        num.append(a**b)
num_set=set(num)
print('ans',len(num_set))
