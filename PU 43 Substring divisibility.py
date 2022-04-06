import timeit
start = timeit.default_timer()
from itertools import permutations
total = 0
l = ['0','1','2','3','4','5','6','7','8','9']
for x in permutations(l):
    j = ''.join(x)
    if int(j[7:10]) % 17 == 0:
        if int(j[6:9]) % 13 == 0:
            if int(j[5:8]) % 11 == 0:
                if int(j[4:7]) % 7 == 0:
                    if int(j[3:6]) % 5 == 0:
                        if int(j[2:5]) % 3 == 0:
                            if int(j[1:4]) % 2 == 0:
                                     total += int(j)
print("Answer is : ", total)
stop = timeit.default_timer()
print("Time taken : ", stop - start)
