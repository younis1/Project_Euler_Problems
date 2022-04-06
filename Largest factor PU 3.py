import timeit
start = timeit.default_timer()
a = 2
b = 600851475143
while a < b:
    if b % a != 0:
        a += 1
    else:
        b = b / a 
print ("Answer is ", a)
stop = timeit.default_timer()
print("Time taken :" , stop - start)
