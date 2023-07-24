tot=1
diff=2
num=1
for rounds in range(1,501):
    for recurr in range(1,5):
        print(num,diff,rounds)
        num+=diff
        tot+=num
    diff+=2
   
print('total',tot)
    
