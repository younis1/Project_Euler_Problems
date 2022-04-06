# First, recall that for x to be divisible by 3, the sum of the digits has to be modulus 3
# Therefore, we recognise that the number digits has to be modulus 3 ... I.e replacing 3 digits, or 6 digits, etc ....
# This is because if it was not, out of the nine combinations, at least 3 will be modulus 3, so a maximum of 6/9 primes (7/10 primes if including 0)
# Furthermore, the sum of the 'constant' digits has to not be divisible by 3
# Note, last digit has to be constant digits (for number not to be even)

# We can replace every digit but the last. If we are changing the first digit, then we do not try the number '0', instead just 1-9
# Therefore for numbers less than 7 digits, we know we only have to replace 3 digits only

def is_prime(number):
    global PRIMES_UNDER_10000
    NUMBER_ROOT = sqrt(number)
    i = 0
    while PRIMES_UNDER_10000[i] <= int(NUMBER_ROOT):
        if (number % PRIMES_UNDER_10000[i] == 0):
            return False
        else:
            i += 1
    return True
    

def generate_primes_under_10000(primes_list):
    primes_list.append(2)
    primes_list.append(3)
    for i in range(5, 10000,2):
        j = 3
        prime = True
        while (j <= int(sqrt(i)) and prime):
            if i % j == 0:
                prime = False
            else:
                j+= 2
            
        if (prime):
            primes_list.append(i)

            
def replace_and_count_primes(number, combinations):
    NUMBERS = [1,2,3,4,5,6,7,8,9]
    counter = 0
    first_prime = 0
    if not (0 in combinations):
        # If first digit is NOT being changed, then also try replacing with 0
        NUMBERS.insert(0, 0)
    for i in NUMBERS:
        replaced_number = ''
        for j in range(len(str(number))):
            if j in combinations:
                replaced_number += str(i)
            else:
                replaced_number += str(number)[j]
        if is_prime(int(replaced_number)):
            counter += 1
            if (first_prime == 0):
                first_prime = replaced_number
    return [counter, first_prime]
        
        

from math import sqrt
from time import time
from itertools import combinations as comb
START = time()
FIRST_PRIME = 56005  # Given in the question
THRESHOLD = 8  # Family of 8 primes needs to be found
NUMBER_OF_DIGITS_REPLACED = 3  # For numbers less than 7 digits
PRIMES_UNDER_10000 = []  # To make prime detection much faster ... works for numbers below 9 digits
MAX_NUMBER = 1000000  # This method works for numbers less than 7 digits
answer = 0  # Changes when answer is found
current_number = FIRST_PRIME
generate_primes_under_10000(PRIMES_UNDER_10000)
print(time() - START)

while (answer == 0 and current_number < MAX_NUMBER):
    current_number += 2
    if (current_number % 3 != 0 and is_prime(current_number)):
        combinations = comb([x for x in range(len(str((current_number))))], NUMBER_OF_DIGITS_REPLACED)
        for x in combinations:
            prime_count, first_prime = replace_and_count_primes(current_number, x)
            if (prime_count == THRESHOLD):
                answer = first_prime

print(answer)
END = time()
print(END - START)



