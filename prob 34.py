def fac(num):
    if num==0:
        return 1
    else:
        return(num*(fac(num-1)))



digit_fac=0

for n in range(11,999999):
    tot=0
    num_list=list(map(int,list(str(n))))
    l=len(num_list)
    for i in range(0,l):
        r=fac(num_list[i])
        tot+=r
    if tot==n:
        print(tot)
        digit_fac+=n
print('total',digit_fac)
