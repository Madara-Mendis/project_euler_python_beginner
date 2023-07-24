n=1#num length
t=9#number of nums in n length
y=10#which digit needed
g=9#substracting part from y
tot=1
while y<1000000:
    y*=10
    x=y-g  #x is number of digits remaining in the relevant n length
    m=x%(n+1)#how many digits remaining to get the correct digit
    num=(x//(n+1))+1#last number concatanate to the chain-number which contain the relevant digit
    d=int((str(num+t))[m-1])#relevant digit
    tot*=d
    t*=10
    n+=1
    g+=(t*n)
print(tot)
    
