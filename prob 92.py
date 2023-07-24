count=4753250
def SDC(x):
    if x==89:
        return 1
    elif x==1:
        return 0
    else:
        str_x=str(x)
        L=len(str_x)
        n=0
        for i in range(L):
            n+=(int(str_x[i]))**2
        print(n,num,count)
        return SDC(n)

num=5530377
while num<10000000:
    if SDC(num)==1:
        count+=1
    num+=1
print('count',count)
#1023870-876996
#1037667-888664
#3859903-3315265
#3925587-3371638
