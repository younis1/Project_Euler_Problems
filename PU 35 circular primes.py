import timeit
start = timeit.default_timer()
from function import isprime,rotatelist
counter  = 1
l = []
for i in range(2,1000000):
    if isprime(i) == 1:
        out = 0
        l.clear()
        for j in  str(i):
            l.append(j)
        for x in range(0,len(l)):
            jo = ''.join(rotatelist(l,x))
            if isprime(int(jo)) != 1:
                out = 1
                break
        if out == 0:
            counter += 1
print("Answer is ", counter)
stop = timeit.default_timer()
print("Time taken : ", stop - start)

