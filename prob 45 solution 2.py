import math
#here i iterate over tranguler numbers from 40756 and check whetehr they are pentogonal and hexagonal  

def check_pentagonal(num):
    n = (math.sqrt(24*num + 1) + 1) % 6
    return n == 0

def check_hexagonal(num):
    n = (math.sqrt(8*num + 1) + 1) % 4
    return n == 0

def find_special_number(start_num):
    num = start_num
    while True:
        triangular = num * (num + 1) // 2
        if check_pentagonal(triangular) and check_hexagonal(triangular):
            return triangular
        num += 1

start_num = 286
special_num = find_special_number(start_num)
print(special_num)
