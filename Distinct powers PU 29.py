import timeit
start = timeit.default_timer()
counter = 0
a = []
for i in range(2,101):
    for j in range(2,101):
        total = i**j
        if total not in a:
            a.append(total)
            counter += 1
stop = timeit.default_timer()
print("Answer is : ", counter)
print("Time taken : ", stop - start)
