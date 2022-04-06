import timeit
start = timeit.default_timer()
a = 1
b = 2
c = 0
counter = 3
while len(str(a)) < 1000 and len(str(b)) < 1000  and len(str(c)) < 1000:
    if len(str(c)) < 1000:
        c = a + b
        counter += 1
    if len(str(a)) < 1000:
        a = b + c
        counter += 1
    if len(str(b)) < 1000:
        b = a +c
        counter += 1
stop = timeit.default_timer()
print(counter)
print(stop - start)
