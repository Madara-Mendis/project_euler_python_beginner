tot=0
for n in range(1,1001):
    tot+=(n**n)
print(tot)
print('last 10 digits',(str(tot))[-10:])
