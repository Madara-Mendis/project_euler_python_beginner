digit_sum=0
import decimal
tot=0
sq=[4,9,16,25,36,49,64,81,100]
for num in range(2,100):
    if not num in sq:
        d=decimal.Decimal(num)
        dot100=decimal.Context(prec=100)
        sq_root=str(d.sqrt(dot100))
        print(sq_root,num)
        dot=sq_root.find('.')
        print(dot)
        digit_100=sq_root[dot+1:(dot+102)]
        print(digit_100)
        for digit in digit_100:
            digit_sum+=int(digit)
        tot+=digit_sum
print('tot',tot)
