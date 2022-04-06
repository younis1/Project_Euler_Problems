import timeit
import math
start =  timeit.default_timer()
a = 0
b = 0
for i in range (1,101):
    a += i
    b += math.pow(i,2)
print("Answer is : ",math.pow(a,2) - b)
stop = timeit.default_timer()
print("Time taken : ",stop - start)

