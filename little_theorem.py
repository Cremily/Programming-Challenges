from math import sqrt
from math import ceil
def does_divide(num,div):
    if num % div == 0:
        return True
    else:
        return False
def is_prime(num):
    if num is not int(num):
        raise TypeError('Primes are in Z!')
    if num < 2:
        return False
    if num == 2:
        return True
    for test_val in range(2,ceil(sqrt(num))+1):
        if does_divide(num,test_val):
            return False
    else:
        return True
def little_prime_test(prime,base):
    divisee = (base ** prime) - base
    if divisee % prime == 0:
        return True
    else:
        return False


def find_pseudo_primes(upper_num,upper_base,lower_base=2,lower_num=2):
    if (lower_base < 2 
    or lower_num < 2):
        raise ValueError("lower bounds must be at least 2!")
    if (upper_num < 3 
    or upper_base < 3):
        raise ValueError("Upper bounds must be at least 3!")
    if ((lower_base != int(lower_base)) 
    or (lower_num != int(lower_num))):
        raise TypeError("numbers must be in Z!")
    primes = []
    number_list = []
    little_not_primes = []
    for x in range(lower_num,upper_num+1):
        number_list.append(x)
        if is_prime(x):
            primes.append(x)
    for base in range(lower_base,upper_base+1):
        for prime_test in range(lower_num,upper_num+1):
            if not little_prime_test(prime_test,base):
                little_not_primes.append(prime_test)
    little_primes = []
    for number in number_list:
        if number not in little_not_primes:
            little_primes.append(number)
    pseudo_primes = []
    for number in little_primes:
        if number not in primes:
            pseudo_primes.append(number)
    return pseudo_primes
print(find_pseudo_primes(2,2))

