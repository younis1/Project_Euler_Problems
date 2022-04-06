import timeit
start = timeit.default_timer()
total = 0
high = 0
acc = 0
for i in range(10,100):
    for j in range(6,100):
        total =i **j
        acc = 0
        for k in str(total):
            acc += int(k)
        if high < acc:
            high = acc
stop = timeit.default_timer()
print("Answer is ", high)
print("Time taken : ",stop - start)
