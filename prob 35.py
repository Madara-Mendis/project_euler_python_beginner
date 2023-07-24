even=[0,2,4,6,8]
num=[]
for odd in range(11,999999,2):
    odd_list=list(map(int,list(str(odd))))
    l=len(odd_list)
    for i in range(0,l):
        if odd_list[i] in even:
            break
    else:
        for p in range(3,odd):
            if odd%p==0:
                break
        else:
            num.append(odd)
print(num)
                
        
