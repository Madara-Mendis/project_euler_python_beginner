tot=5
for i in range(5,2000000,2):
    for n in range(3,i//2,2):
        if i%n==0:
            break
    else:
        print(i)
        tot+=i
print("total:",tot)
