import timeit
start = timeit.default_timer()
a = 0
a = 2 ** 1000
total = 0
for i in str(a) :
    total += int(i)
stop = timeit.default_timer()
print(total)
print(stop - start)

