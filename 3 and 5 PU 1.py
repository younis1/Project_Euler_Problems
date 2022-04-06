import timeit
start= timeit.default_timer()
total = 0
for i in range(1,1000):
    if i % 3 == 0 or i %5 == 0:
        total += i
print("Answer is : ", total)
stop = timeit.default_timer()
print("Time taken : ", stop - start)
