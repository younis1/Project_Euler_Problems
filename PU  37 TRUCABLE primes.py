import timeit
start= timeit.default_timer()
from function import isprime
finalcounter = 0
total = 0
current = 0
ocurrent = 0
num = 9
while finalcounter < 11:
    num += 2
    b = 0
    a = str(num)
    leng = len(a)
    out  = 0
    if isprime(num) == 1:
        while b < leng:
            b += 1
            current = int(a[:b])
            ocurrent = int(a[b-1:])
            if isprime(current) == 0:
                out = 1
                break
            elif isprime(ocurrent) == 0:
                out = 1
                break
        if out == 0:
            print(num)
            total += num
            finalcounter += 1   
print("Answer is ", total)
stop = timeit.default_timer()
print("Time taken : ", stop - start)


