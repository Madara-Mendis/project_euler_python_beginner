def factorial(n):
    if n==1:
        return 1
    else:
        return(n*(factorial(n-1)))
tot=0
num=str(factorial(100))
for i in num:
    tot+=int(i)
print('total',tot)
