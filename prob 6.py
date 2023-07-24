tot_1=tot_2=0
for num in range(1,101):
    sq=num**2
    tot_1+=sq #calculating sum of squares of first 100 numbers
    tot_2+=num #calculating sum of first 100 numbers
diff=(tot_2**2)-tot_1
print("difference =",diff)
