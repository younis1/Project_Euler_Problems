import timeit
start = timeit.default_timer()
binary =  0
total = 0 
for i in range(1,1000000):
    binary = bin(i)
    binary = binary[2:]
    if str(i) == str(i)[::-1] and binary == binary[::-1]:
        total += i
print("Answer is ", total)
stop = timeit.default_timer()
print("Time taken : ", stop - start)
