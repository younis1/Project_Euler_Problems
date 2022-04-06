from function import totalfactors
import timeit
start = timeit.default_timer()
amcounter = 0
number  = 0
differencea = 0
for i in range(10,10001):
    number = totalfactors(i)
    if totalfactors(number) == i and number != i :
        amcounter += i
        differencea =0
        differencea = timeit.default_timer()
        print("amicable number", i)
        if differencea >= 5.00000:
            break
stop = timeit.default_timer()
print(amcounter)
print(stop - start )
