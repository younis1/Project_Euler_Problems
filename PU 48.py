import timeit
start = timeit.default_timer()
answer = 0
total= 0
for i in range(1,1001):
    answer= i**i
    total += answer
a =  len(str(total))
b = 0
final = ''
for i in str(total):
    b += 1
    if b > (a- 10):
        final += (i)
print(final, " is the final answer ")
stop = timeit.default_timer()
print(" time taken : ", (stop - start))
