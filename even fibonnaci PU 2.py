import timeit
start = timeit.default_timer()
a = 1
b = 1
total = 0
while a  < 4000000 and b < 4000000 :
    a += b
    b += a
    if a % 2 == 0:
        total += a
    if b % 2 == 0:
        total += b
print("Answer is : ", total)
stop = timeit.default_timer()
print("Time taken : ", stop - start)
