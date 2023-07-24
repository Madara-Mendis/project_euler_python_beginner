digit_fifth=0

for n in range(11,999999):
    tot=0
    num_list=list(map(int,list(str(n))))
    l=len(num_list)
    for i in range(0,l):
        tot+=(num_list[i]**5)
    if tot==n:
        print(tot)
        digit_fifth+=n
print('total',digit_fifth)
