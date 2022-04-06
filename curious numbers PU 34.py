from function import exc_num
import timeit
start = timeit.default_timer()
total = 0
finaltotal = 0
acc = 3
dif = 0
while dif < 5:
    dif = timeit.default_timer()
    total = 0
    acc += 1
    for i in str(acc):
        total += exc_num(int(i))
    if total == acc:
        finaltotal += total
        dif = 0
print("Answer is : ", finaltotal)
stop = timeit.default_timer()
print("Time taken : ", stop - start)
