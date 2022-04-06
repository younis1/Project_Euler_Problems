import timeit
start = timeit.default_timer()
from itertools import permutations
a = ['0','1','2','3','4','5','6','7','8','9']
ac = 0
b = 0
for i in permutations(a):
    ac += 1
    if ac == 1000000:
     b = ''.join(i)
     break
print("Answer is : ", b)
stop = timeit.default_timer()
print("Time taken : ", stop - start)
