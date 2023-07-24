palindrome=[]
a=999
while a>900:#largest product is created from product of largest numbers
    b=a
    while b>900:
        product=a*b
        pro=str(product)#converting int value into string
        pro_reverse= pro[::-1]#taking the reverse of the number
        if pro==pro_reverse:
            palindrome.append(product)#creating a list of first large palindromes
            print(palindrome)
            b-=1
        else:
            b-=1
    else:
        a-=1
print("largest palindrome:",max(palindrome))#selecting the largest palindrome from the list above
