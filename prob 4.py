f=[]
a=999
while a>900:
    b=a
    while b>900:
        #print(b)
        product=a*b
        pro=str(product)
        if(pro[0]==pro[-1]):
            print("done 1")
            if(pro[1]==pro[-2]):
                print("done 2")
                if(pro[2]==pro[-3]):
                    print(a,b)
                    print(product)
                    f.append(product)
                    r=set(f)
                    print(r)
                    b-=1
                    #a=b=99
                    #break
                else:
                    b-=1
            else:
                b-=1
        else:
            b-=1
    else:
        a-=1
print(max(r))
print("end")
                
                
                
