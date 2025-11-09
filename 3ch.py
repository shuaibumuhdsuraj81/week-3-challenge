#large power

def large_power(base, exponent):
    result = base ** exponent
    if result > 5000:
        print('True')
    else:
        print('False')
print(large_power(9, 5)) 


def large_power(base, exponent):
    return base ** exponent > 5000
print(large_power(5, 9))



#DIVISIBLE BY TEN
def divisible_by_ten(num):
    remainder = num % 10
    if remainder == 0:
        print('True')
    else:
        print('False')
print(divisible_by_ten(21))

def divisibleby_ten(num):
    return num % 10 == 0
print(divisibleby_ten(19))