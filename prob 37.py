tot=0
count=0
x=21
def Isprime(n):
    for i in range(2,n):
        if n%i==0:
            return 0
            break
    else:
        return 1
while x>0:
    str_x=str(x)
    length=len(str_x)
    if not (str_x[0]=='1' or str_x[-1]=='1'):
            for i in range(length):#checking whether there is an even number in any index within the number(x)
                if int(str_x[i]) in [0,2,4,6,8]:
                    break
            else:
                if Isprime(x)==1:
                    #print(x)
                    y=1
                    while y<length:
                        remove_left=int(str_x[y:])
                        remove_right=int(str_x[:length-y])
                        if Isprime(remove_left)==1 and Isprime(remove_right)==1:
                            #print(remove_left)
                            #print(remove_right)
                            y+=1
                            if y==length:
                                tot+=x
                                count+=1
                                print(x,count)
                        else:
                            break
    if count==11:
        print(tot)
        break
    print(x)
    x+=2
            
